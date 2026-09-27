from fastapi import APIRouter, Depends, HTTPException
from app.core.orchestrator import AIOrchestrator, ChatRequest, ChatResponse

router = APIRouter()
orchestrator = AIOrchestrator()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = orchestrator.process_query(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
