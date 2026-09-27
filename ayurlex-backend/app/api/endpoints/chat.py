import time
from fastapi import APIRouter, Request, HTTPException
from app.schemas.chat import ChatRequest
from app.schemas.common import StandardResponse, AnalysisMetadata, SourceCitation

router = APIRouter()

@router.post("/chat", response_model=StandardResponse)
async def chat_endpoint(request: ChatRequest, req: Request):
    """
    Process a chat message, search the knowledge base, and return a synthesized response.
    """
    start_time = time.time()
    
    # Validation logic here
    if not request.messages:
        raise HTTPException(status_code=400, detail="Messages list cannot be empty")

    last_msg = request.messages[-1].content

    # Mock response to show structured json format
    process_time_ms = (time.time() - start_time) * 1000

    return StandardResponse(
        answer=f"This is a simulated AI response to: '{last_msg}'. In production, this would call the intelligence engine.",
        language="English",
        sources=[
            SourceCitation(id="src1", title="Charaka Samhita, Sutrasthana", snippet="...", confidenceScore=0.92)
        ],
        citations=["[1] Charaka Samhita"],
        confidence=0.88,
        limitations=["Information is based on historical texts and requires clinical validation."],
        evidence_gaps=["No recent double-blind trials available for this specific formulation."],
        analysis_metadata=AnalysisMetadata(
            processing_time_ms=process_time_ms,
            model_version="ayurlex-core-1.0",
            tokens_used=120
        )
    )

from fastapi.responses import StreamingResponse
from app.ai.orchestrator import ai_orchestrator

@router.post("/chat/stream")
async def chat_stream_endpoint(request: ChatRequest, req: Request):
    """
    Real-time streaming endpoint for chat interactions using Server-Sent Events (SSE).
    """
    if not request.messages:
        raise HTTPException(status_code=400, detail="Messages list cannot be empty")
        
    last_msg = request.messages[-1].content
    session_context = {} # In reality, built from previous messages or memory_service
    
    # We pass the generator to StreamingResponse
    # media_type text/event-stream ensures proper SSE parsing on the client
    return StreamingResponse(
        ai_orchestrator.stream_workflow(last_msg, session_context),
        media_type="text/event-stream"
    )
