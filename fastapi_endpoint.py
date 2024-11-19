from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from pydantic import BaseModel
from fastapi import HTTPException
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from huggingface_hub import login

# Replace with your Hugging Face token
login("HUGGINGFACE_API")

# FastAPI app setup
app = FastAPI()

# middlewares
app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'], 
    allow_credentials=True, 
    allow_methods=['*'], 
    allow_headers=['*'], 
)

# Initialize the model and tokenizer (LLAMA)
class QuestionAnsweringModel:
    def __init__(self):
        self.tokenizer = None
        self.model = None

    def load_model(self):
        """Load LLAMA model and tokenizer"""
        model_name = "meta-llama/Llama-3.2-1B-Instruct"   
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.eval()

    def predict(self, question: str, temperature: float = 0.7) -> str:
        """Run the model to answer a question with adjustable temperature"""
        if not self.model:
            raise HTTPException(status_code=400, detail="Model is not loaded")
        
        inputs = self.tokenizer(question, return_tensors="pt")
        
        # Generate text with adjusted temperature
        outputs = self.model.generate(
            inputs["input_ids"], 
            max_length=200, 
            temperature=temperature,  # Adjust temperature here
            top_k=50,  # You can also adjust other parameters like top_k or top_p for more control
            top_p=0.95
        )
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return answer
    
# Pydantic model for input and output
class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

# Load model
qa_model = QuestionAnsweringModel()

# FastAPI routes
@app.get('/')
def index():
    return {'message': 'Welcome to the LLAMA Question Answering API!'}

@app.post('/answer')
async def get_answer(question: Question) -> Answer:
    """
    Example post request body:
    {
        "question": "What is the capital of France?"
    }
    Example response:
    {
        "answer": "The capital of France is Paris."
    }
    """
    answer = qa_model.predict(question.question)
    return Answer(answer=answer)

# Load model asynchronously on startup
@app.on_event("startup")
async def startup():
    qa_model.load_model()

# Set up the FastAPI app to run on a public URL via ngrok
port = 8004
ngrok_tunnel = ngrok.connect(port)
print(f"Public URL: {ngrok_tunnel.public_url}")

nest_asyncio.apply()
uvicorn.run(app, port=port)