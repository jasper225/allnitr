from fastapi import FastAPI
from app.api.v1.endpoints import summarize, quiz, upload

app = FastAPI(title="ExamSqueeze - MVP")

app.include_router(summarize.router, prefix="/api/v1")
app.include_router(quiz.router, prefix="/api/v1")
app.include_router(upload.router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
