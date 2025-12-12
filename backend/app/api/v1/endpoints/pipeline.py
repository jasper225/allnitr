from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_parser import extract_text_from_file
from app.services.quiz_maker import generate_quiz
from app.services.summarizer import simple_summarize, extract_bullets

router = APIRouter()

@router.post("/pipeline/")
async def pipeline(file: UploadFile = File(...), num_mcq: int = 5, num_tf: int = 5, max_sentences: int = 5):
    try:
        text = await extract_text_from_file(file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to extract text from file: {str(e)}")
    
    summary = simple_summarize(text, max_sentences=max_sentences)
    bullets = extract_bullets(summary)

    quiz = generate_quiz(text, num_mcq=num_mcq, num_tf=num_tf)

    return {
        "summary": summary,
        "bullets": bullets,
        "quiz": quiz
    }