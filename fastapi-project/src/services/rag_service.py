from utils.pdf_loader import extract_text_from_pdf
from vectorstore.faiss_store import FAISSStore
from services.gemini_service import GeminiService


class RAGService:
    def __init__(self):
        self.vectorstore = FAISSStore()
        self.llm = GeminiService()

    
    def upload_pdf(self, file_bytes):
        """
        Extract text from PDF and store embeddings in FAISS
        """

      
        self.vectorstore.reset()

        
        chunks = extract_text_from_pdf(file_bytes)

        
        self.vectorstore.add_texts(chunks)

        return {
            "message": "PDF uploaded and indexed successfully",
            "chunks": len(chunks)
        }


    
    def ask_question(self, question: str):
        docs = self.vectorstore.search(question, k=3)

        
        if not docs:
            return {
                "answer": "No answer found in PDF",
                "context_used": []
            }

        context = "\n".join(docs)

        prompt = f"""
    Answer the question ONLY using the context below.
    If the answer is not present, say "No answer found in PDF".

    Context:
    {context}

    Question:
    {question}
    """

        answer = self.llm.generate(prompt).strip()

        return {
            "answer": answer,
            "context_used": docs
        }