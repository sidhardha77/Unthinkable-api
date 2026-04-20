from fastapi import APIRouter, UploadFile, File
from models.qa_models import QuestionRequest, APIResponse, AskResponse
from services.rag_service import RAGService

router = APIRouter(prefix="/qa", tags=["QA"])

rag_service = RAGService()



@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()

        result = rag_service.upload_pdf(file_bytes)

        return {
            "success": True,
            "message": result["message"],
            "chunks": result["chunks"]
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }



@router.post("/ask", response_model=APIResponse)
async def ask_question(req: QuestionRequest):
    try:
        # Check if any PDF is uploaded
        if not rag_service.vectorstore.texts:
            return APIResponse(
                success=False,
                message="No PDF uploaded yet",
                data=None
            )

        # Validate question
        if not req.question or not req.question.strip():
            return APIResponse(
                success=False,
                message="Question cannot be empty",
                data=None
            )

        # Get answer from service
        result = rag_service.ask_question(req.question)

        # Handle no answer case safely
        if not result or "answer" not in result:
            return APIResponse(
                success=False,
                message="Failed to generate answer",
                data=None
            )

        return APIResponse(
            success=True,
            message="Answer generated",
            data=AskResponse(
                answer=result.get("answer", "No answer found in PDF"),
                context_used=result.get("context_used", [])
            )
        )

    except Exception as e:
        print("ASK ERROR:", str(e)) 

        return APIResponse(
            success=False,
            message="Something went wrong",
            data=None
        )