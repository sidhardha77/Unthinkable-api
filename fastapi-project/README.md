# AI PDF Question Answering API

This project is an AI-powered system that allows users to upload a PDF and ask questions based on its content.

It uses FastAPI, FAISS, and Google Gemini AI to retrieve relevant information from documents and generate accurate answers.

If the answer is not found in the PDF, the system responds with:
"No answer found in PDF"

---

# Features

- Upload PDF files
- Ask questions based on uploaded documents
- Semantic search using FAISS vector database
- AI-generated answers using Gemini
- Safe fallback when answer is not found
- Separate APIs for upload and question handling
- Clean RAG (Retrieval Augmented Generation) architecture

---

# Project Structure

services/
   rag_service.py        - Core RAG logic
   gemini_service.py     - Gemini AI integration

routes/
   qa.py                 - API endpoints

models/
   qa_models.py         - Request and response models

vectorstore/
   faiss_store.py       - Vector database implementation

utils/
   pdf_loader.py        - PDF text extraction

---

# API Endpoints

---

## 1. Upload PDF

Endpoint:
POST /qa/upload

Description:
Uploads a PDF file and stores its content in the vector database for later question answering.

Request:
form-data

file: PDF file

Response:
```json
{
  "success": true,
  "message": "PDF uploaded and indexed successfully",
  "chunks": 42
}



 ## 2. Ask Question
Endpoint:
POST /qa/ask
Description
Ask a question based on the uploaded PDF content.
Request
{
  "question": "What is machine learning?"
}
Response (Answer Found)
{
  "success": true,
  "message": "Answer generated",
  "data": {
    "answer": "Machine learning is a branch of artificial intelligence that allows systems to learn from data.",
    "context_used": [
      "relevant chunk 1",
      "relevant chunk 2"
    ]
  }
}
Response (No Answer Found)
{
  "success": true,
  "message": "Answer generated",
  "data": {
    "answer": "No answer found in PDF",
    "context_used": []
  }
}
