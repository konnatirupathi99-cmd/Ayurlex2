from fastapi import APIRouter, HTTPException
from app.models.requests import AnalysisRequest
from app.models.responses import IntelligenceReport
from app.services.intelligence_engine import generate_intelligence_report
import uuid

router = APIRouter()

@router.post("/", response_model=IntelligenceReport)
async def create_analysis(request: AnalysisRequest):
    try:
        report = await generate_intelligence_report(request)
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{analysis_id}")
async def get_analysis(analysis_id: str):
    # Placeholder for retrieving a saved report
    return {"analysis_id": analysis_id, "status": "retrieved"}

@router.get("/history")
async def get_history():
    # Placeholder for retrieving analysis history
    return {"history": []}
