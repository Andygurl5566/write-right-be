from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_service import correct_text
from pydantic import BaseModel



# Initialize the FastAPI application instance
app = FastAPI()

# CORS - # Allows React frontend (running on a different URL/port) to safely communicate with this FastAPI backend.
origins = [
    "http://localhost:5173",  # Vite frontend
    "http://localhost:3000",
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


# Defines a root path GET endpoint
@app.get("/")
def read_root():
    return {"status": "success", "message": "FastAPI is initialized!"}

# Route for submitting text for correction
@app.post("/correct")
async def correct(request: CorrectionRequest):

    print("Received:", request.text)

    corrected = await correct_text(request.text)

    print("Model returned:", corrected)

    return corrected