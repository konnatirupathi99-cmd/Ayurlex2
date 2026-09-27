from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class OrchestratorState(BaseModel):
    query: str
    language: str
    jurisdiction: str
    entities: List[str] = Field(default_factory=list)
    modules_used: List[str] = Field(default_factory=list)
    sources: List[str] = Field(default_factory=list)
    evidence: List[Dict[str, Any]] = Field(default_factory=list)
    conflicts: List[str] = Field(default_factory=list)
    confidence: str
    limitations: List[str] = Field(default_factory=list)
    answer: str
