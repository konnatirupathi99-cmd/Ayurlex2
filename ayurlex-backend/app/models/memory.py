from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid

class Message(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    role: str # "user", "assistant", "system"
    content: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    tokens: Optional[int] = None

class ShortTermMemory(BaseModel):
    session_id: str
    user_id: str
    current_task: Optional[str] = None
    current_language: str = "en"
    current_jurisdiction: str = "International"
    current_analysis_context: Dict[str, Any] = Field(default_factory=dict)
    messages: List[Message] = Field(default_factory=list)
    summary: Optional[str] = None
    last_updated: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

class LongTermMemory(BaseModel):
    user_id: str
    preferred_language: Optional[str] = None
    frequently_used_jurisdiction: Optional[str] = None
    interface_preferences: Dict[str, Any] = Field(default_factory=dict)
    saved_analysis_preferences: Dict[str, Any] = Field(default_factory=dict)
    last_updated: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

class MemoryRetrievalRequest(BaseModel):
    user_id: str
    session_id: Optional[str] = None
    query: Optional[str] = None
    include_long_term: bool = True
    include_short_term: bool = True
