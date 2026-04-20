# 📄 Knowledge-Base Search Engine (RAG System)

This project is a **Retrieval-Augmented Generation (RAG)** based system that allows users to upload a PDF and ask questions based on its content.

The system retrieves relevant information from the document using vector search and generates accurate answers using AI.

---

##  Tech Stack

* **Backend:** FastAPI
* **Frontend:** Angular
* **Vector Database:** FAISS
* **LLM:** Google Gemini API

---

## ⚙️ Features

* Upload PDF documents
* Ask questions based on uploaded content
* Semantic search using FAISS
* AI-generated answers using Gemini
* Returns **"No answer found in PDF"** if context is missing
* Clean RAG pipeline (Retrieve → Generate)

---

## How It Works

1. PDF is uploaded
2. Text is extracted and split into chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. User asks a question
6. Relevant chunks are retrieved
7. Gemini generates answer based on context

---

## 📁 Project Structure

```
fastapi-project/
 ├── src/
 │   ├── services/
 │   │   ├── rag_service.py
 │   │   ├── gemini_service.py
 │   ├── routes/
 │   │   ├── qa.py
 │   ├── models/
 │   │   ├── qa_models.py
 │   ├── utils/
 │   │   ├── pdf_loader.py
 │   ├── vectorstore/
 │   │   ├── faiss_store.py
 │   └── main.py

rag-ui/
 ├── src/
 ├── package.json
```

---

## 🔗 API Endpoints

### 1. Upload PDF

**POST** `/qa/upload`

**Request:**
Form-data

* file: PDF

**Response:**

```json
{
  "success": true,
  "message": "PDF uploaded and indexed successfully",
  "chunks": 42
}
```

---

### 2. Ask Question

**POST** `/qa/ask`

**Request:**

```json
{
  "question": "What is machine learning?"
}
```

**Response (Answer Found):**

```json
{
  "success": true,
  "message": "Answer generated",
  "data": {
    "answer": "Machine learning is a branch of artificial intelligence...",
    "context_used": ["chunk1", "chunk2"]
  }
}
```

**Response (No Answer):**

```json
{
  "success": true,
  "message": "Answer generated",
  "data": {
    "answer": "No answer found in PDF",
    "context_used": []
  }
}
```

---

## 🛠️ Setup Instructions

### 🔹 1. Clone Repository

```
git clone https://github.com/sidhardha77/Unthinkable-api.git
cd Unthinkable-api
```

---

### 🔹 2. Backend Setup (FastAPI)

```
cd fastapi-project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

### 🔹 3. Set Environment Variables

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

###  4. Run Backend

```
uvicorn src.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 5. Frontend Setup (Angular)

```
cd rag-ui
npm install
ng serve
```

Frontend runs at:

```
http://localhost:4200
```

---

---



* Document QA systems
* Knowledge base search
* AI-powered document analysis

---

 Conclusion

This project demonstrates how combining **vector search (FAISS)** with **LLMs (Gemini)** enables accurate and context-aware question answering over documents.

---
