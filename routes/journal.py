from fastapi import APIRouter
from services.ai_service import correct_text
from services.correction_service import add_indices
from schemas import JournalAnalysisRequest, JournalAnalysisResponse

router = APIRouter()


@router.post("/analyze", response_model=JournalAnalysisResponse)
async def analyze_journal(data: JournalAnalysisRequest):

    text = data.text

    # AI anlysis of the text
    analysis = await correct_text(text)
    
    #Backend adds start/end indices to each mistake for frontend highlighting
    analysis = add_indices(
        text,
        analysis
    )

    return analysis