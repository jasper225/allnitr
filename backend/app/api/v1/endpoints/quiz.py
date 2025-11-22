from fastapi import APIRouter
from pydantic import BaseModel
from app.services.quiz_maker import generate_quiz

router = APIRouter()

class QuizReq(BaseModel):
    text: str
    num_mcq: int = 5
    num_tf: int = 5

@router.post("/quiz")
def quiz(req: QuizReq):
    quiz = generate_quiz(req.text, num_mcq=req.num_mcq, num_tf=req.num_tf)
    return quiz
