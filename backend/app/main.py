from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import summarize, quiz, upload, pipeline

app = FastAPI(title="allnitr - MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarize.router, prefix="/api/v1")
app.include_router(quiz.router, prefix="/api/v1")
app.include_router(upload.router, prefix="/api/v1")
app.include_router(pipeline.router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Welcome to allnitr MVP Backend!"}
