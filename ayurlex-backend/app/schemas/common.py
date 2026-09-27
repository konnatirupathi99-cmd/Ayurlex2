from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict

class SourceCitation(BaseModel):
    id: str
    title: str
    url: Optional[str] = None
    snippet: Optional[str] = None
    confidenceScore: Optional[float] = None

class AnalysisMetadata(BaseModel):
    processing_time_ms: float
    model_version: str
    tokens_used: int

class StandardResponse(BaseModel):
    answer: str
    language: str = "English"
    sources: List[SourceCitation] = Field(default_factory=list)
    citations: List[str] = Field(default_factory=list)
    confidence: float
    limitations: List[str] = Field(default_factory=list)
    evidence_gaps: List[str] = Field(default_factory=list)
    analysis_metadata: AnalysisMetadata
