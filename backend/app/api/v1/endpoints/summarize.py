from fastapi import APIRouter
from pydantic import BaseModel
from app.services.summarizer import simple_summarize, extract_bullets

router = APIRouter()

class SummarizeReq(BaseModel):
    text: str
    max_sentences: int = 5

@router.post("/summarize")
def summarize(req: SummarizeReq):
    summary = simple_summarize(req.text, max_sentences=req.max_sentences)
    bullets = extract_bullets(summary)
    return {"summary": summary, "bullets": bullets}