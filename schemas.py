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
class FlashcardCreate(BaseModel):
    front: str
    back: str
    language: str = "German"


class FlashcardUpdate(BaseModel):
    front: str | None = None
    back: str | None = None
    language: str | None = None
    mastered: bool | None = None


class FlashcardResponse(BaseModel):
    id: int
    front: str
    back: str
    language: str
    mastered: bool

    model_config = {
        "from_attributes": True,
    }
