from fastapi import APIRouter, UploadFile, File
from app.services.file_parser import extract_text_from_file

router = APIRouter()

@router.post("/upload/")
async def upload_material(file: UploadFile = File(...)):
    text = await extract_text_from_file(file)
    return {"text": text}