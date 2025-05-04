# tesla-rag-chatbot
Retrieval-Augmented Generation chatbot for Tesla vehicle documentation

# Tesla RAG Chatbot

A Retrieval-Augmented Generation system for answering questions about Tesla vehicles.

## Features

- Answers questions using official Tesla documentation
- Supports Model S, 3, X, Y and Cybertruck
- Technical and service information

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download Tesla manuals to `data/raw_documents`
4. Run preprocessing: `python src/data_processing/process.py`
5. Start the app: `uvicorn src.app.main:app --reload`

## API Usage

POST `/ask` with JSON body: `{"question": "How do I reset my Tesla screen?"}`