from fastapi import APIRouter, HTTPException, Query, Body, Path
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from app.models.memory import ShortTermMemory, LongTermMemory, MemoryRetrievalRequest
from app.services.memory_service import memory_service

router = APIRouter(prefix="/memory", tags=["memory"])

class AddMessageRequest(BaseModel):
    role: str
    content: str

class UpdateContextRequest(BaseModel):
    current_task: Optional[str] = None
    current_language: Optional[str] = None
    current_jurisdiction: Optional[str] = None
    current_analysis_context: Optional[Dict[str, Any]] = None

class UpdateLTMRequest(BaseModel):
    preferred_language: Optional[str] = None
    frequently_used_jurisdiction: Optional[str] = None
    interface_preferences: Optional[Dict[str, Any]] = None
    saved_analysis_preferences: Optional[Dict[str, Any]] = None

@router.post("/{user_id}/{session_id}/message", response_model=ShortTermMemory)
async def add_message(
    user_id: str = Path(...),
    session_id: str = Path(...),
    request: AddMessageRequest = Body(...)
):
    """Add a new message to the short term memory, managing context window automatically."""
    return memory_service.add_message(user_id, session_id, request.role, request.content)

@router.patch("/{user_id}/{session_id}/context", response_model=ShortTermMemory)
async def update_context(
    user_id: str = Path(...),
    session_id: str = Path(...),
    request: UpdateContextRequest = Body(...)
):
    """Update short-term memory context parameters."""
    return memory_service.update_context(
        user_id=user_id,
        session_id=session_id,
        task=request.current_task,
        language=request.current_language,
        jurisdiction=request.current_jurisdiction,
        analysis_context=request.current_analysis_context
    )

@router.patch("/{user_id}/long-term", response_model=LongTermMemory)
async def update_long_term_memory(
    user_id: str = Path(...),
    request: UpdateLTMRequest = Body(...)
):
    """Update long-term user preferences safely without storing sensitive info."""
    preferences = request.model_dump(exclude_unset=True)
    return memory_service.update_ltm(user_id, preferences)

@router.post("/retrieve", response_model=Dict[str, Any])
async def retrieve_relevant_memory(request: MemoryRetrievalRequest):
    """Allow AI orchestrator to request only the relevant subset of memory."""
    return memory_service.retrieve_relevant_memory(request)

@router.delete("/{user_id}/{session_id}", response_model=Dict[str, Any])
async def delete_session_memory(user_id: str = Path(...), session_id: str = Path(...)):
    """Delete a specific conversation session."""
    success = memory_service.delete_session_memory(user_id, session_id)
    if not success:
        raise HTTPException(status_code=404, detail="Session memory not found")
    return {"status": "success", "message": "Session memory deleted"}

@router.delete("/{user_id}/long-term", response_model=Dict[str, Any])
async def clear_long_term_memory(user_id: str = Path(...)):
    """Clear all long-term preferences for a user."""
    success = memory_service.clear_long_term_memory(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Long-term memory not found")
    return {"status": "success", "message": "Long-term memory cleared"}
