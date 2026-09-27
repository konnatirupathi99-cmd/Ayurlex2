from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class RetrievedEvidence(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    evidence_id: str
    document_id: str = Field(default="", alias="source_id")
    chunk_id: Optional[str] = None
    source_title: str = Field(default="", alias="title")
    source_name: Optional[str] = None
    source_type: Optional[str] = None
    category: str
    jurisdiction: str = "International"
    jurisdiction_scope: Optional[str] = None
    language: str
    section: Optional[str] = None
    page_number: Optional[str] = None
    content: str
    original_content: Optional[str] = None
    relevance_score: float
    match_type: Optional[str] = None
    retrieval_method: Optional[str] = None
