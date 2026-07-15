from datetime import datetime

from pydantic import BaseModel


class JournalAnalysisRequest(BaseModel):
    text: str


class MistakeResponse(BaseModel):
    original: str
    corrected: str
    explanation: str
    category: str
    start: int | None = None
    end: int | None = None


class JournalAnalysisResponse(BaseModel):
    text: str
    mistakes: list[MistakeResponse]


class JournalEntryResponse(BaseModel):
    id: int
    original_text: str
    corrected_text: str
    mistakes: list[MistakeResponse]
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }