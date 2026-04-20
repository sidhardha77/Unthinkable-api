from pydantic import BaseModel
from typing import List



# REQUEST MODEL
class QuestionRequest(BaseModel):
    question: str



# RESPONSE MODELS
class QAResponse(BaseModel):
    question: str
    answer: str


class AskResponse(BaseModel):
    answer: str
    context_used: List[str]


class APIResponse(BaseModel):
    success: bool
    message: str | None = None
    data: AskResponse | None = None