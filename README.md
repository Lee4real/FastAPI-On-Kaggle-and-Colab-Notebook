# FastAPI On Kaggle & Colab Notebook

This project demonstrates how to deploy a FastAPI application on Kaggle and Google Colab notebooks. The application is designed to answer questions using the LLaMA model from Hugging Face.

## Requirements

To run this project, you need to install the following packages:

- `pyngrok` for creating a public URL for the application
- `fastapi` for building the API
- `nest-asyncio` for handling asynchronous operations
- `uvicorn` for running the API
- `transformers` for using the LLaMA model

You can install these packages using pip:

```
pip install pyngrok fastapi nest-asyncio uvicorn transformers
```

## Setting Up the Environment

To set up the environment for this project, follow these steps:

1. Install the required packages as mentioned above.
2. Create a new Kaggle notebook or Google Colab notebook.
3. In the notebook, install `pyngrok` using the following command:

```
!pip install pyngrok
```

4. Configure your `ngrok` account by running the following command:

```
!ngrok config add-authtoken YOUR_NGROK_API_TOKEN
```

Replace `YOUR_NGROK_API_TOKEN` with your actual ngrok API token.

## Running the Application

To run the application, follow these steps:

1. Clone this repository or copy the contents of `fastapi_endpoint.py` into a new notebook cell.
2. Run the cell to execute the application.
3. The application will start and print a public URL that you can use to access the API.

## Testing the Application

To test the application, follow these steps:

1. Clone this repository or copy the contents of `test_fastapi.py` into a new notebook cell.
2. Replace `YOUR_NGROK_URL` with the public URL printed by the application.
3. Run the cell to execute the test.
4. The test will send a POST request to the API with a question and print the response.

## Using the Application

To use the application, you can send a POST request to the public URL with a JSON body containing the question you want to ask. The API will respond with the answer to the question.

Example request body:

```json
{
  "question": "What is the capital of France?"
}
```

Example response:

```json
{
  "answer": "The capital of France is Paris."
}
```
