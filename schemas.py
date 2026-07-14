from pydantic import BaseModel


class JournalAnalysisRequest(BaseModel):
    text: str


class MistakeResponse(BaseModel):
    original: str
    corrected_text: str
    explanation: str
    category: str
    start: int | None = None
    end: int | None = None


class JournalAnalysisResponse(BaseModel):
    text: str
    mistakes: list[MistakeResponse]