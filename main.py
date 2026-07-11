from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from database import Base, engine
import models

# Initialize the FastAPI application instance
app = FastAPI()

Base.metadata.create_all(bind=engine)

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

# Defines a root path GET endpoint
@app.get("/")
def read_root():
    return {"status": "success", "message": "FastAPI is initialized!"}


# Test connection with Supabase | 
# To test connection, start BE using fastapi dev main.py command, 
# navigate to http://127.0.0.1:8000/db-test in browser 
# successful response will show {"status":"connected","result":1}

@app.get("/db-test")
def database_test():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            
        return {
            "status": "connected",
            "result": result.scalar()
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": "Database connection failed" 
        }