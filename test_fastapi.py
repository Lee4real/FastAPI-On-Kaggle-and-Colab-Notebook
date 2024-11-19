import requests
import json

# Define the FastAPI public URL (replace with your actual ngrok URL)
NGROK_URL = "YOUR_NGROK_URL"
url = f"{NGROK_URL}/answer"

# Define the payload (your question)
data = {
    "question": "what is the capital of france?"
}

# Send a POST request
response = requests.post(url, json=data)

# Check the response status
if response.status_code == 200:
    # If the request is successful, print the response (answer from the model)
    answer = response.json()
    print(f"Answer: {answer['answer']}")
else:
    print(f"Request failed with status code {response.status_code}")
