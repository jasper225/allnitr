from fastapi import APIRouter, UploadFile, File
from app.services.file_parser import extract_text_from_file
from app.services.summarizer import simple_summarize, extract_bullets
from app.services.quiz_maker import generate_quiz

router = APIRouter()

@router.post("/upload/")
async def upload_material(file: UploadFile = File(...)):
    text = await extract_text_from_file(file)
    summary = simple_summarize(text, max_sentences=5)
    bullets = extract_bullets(summary)
    quiz = generate_quiz(text, num_mcq=5, num_tf=5)
    
    return {"text": text,
            "summary": summary,
            "bullets": bullets,
            "quiz": quiz
            }