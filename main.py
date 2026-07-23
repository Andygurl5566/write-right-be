from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.ai_service import correct_text
from pydantic import BaseModel

from database import Base, engine
import models
from routes import journal, flashcards, flashcard_sets



# Initialize the FastAPI application instance
app = FastAPI()

Base.metadata.create_all(bind=engine)

# CORS - # Allows React frontend (running on a different URL/port) to safely communicate with this FastAPI backend.
origins = [
    "http://localhost:5173",  # Vite frontend
    "http://localhost:5173/",
    "http://localhost:5173/flashcards",
    "http://localhost:3000",
    "http://localhost:5174",
    "http://localhost:5174/"
    "http://localhost:5174/flashcards"
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CorrectionRequest(BaseModel):
    text: str


# Include the journal router for handling journal-related endpoints
# journal/analyze endpoint for journal corrections
app.include_router(
    journal.router,
    prefix="/journal",
    tags=["Journal"],
)

app.include_router(
    flashcards.router,
    prefix="/flashcards",
    tags=["Flashcards"],
)

app.include_router(
    flashcard_sets.router,
    prefix="/flashcard-sets",
    tags=["Flashcard Sets"],
)


# Defines a root path GET endpoint
@app.get("/")
def read_root():
    return {"status": "success", "message": "FastAPI is initialized!"}