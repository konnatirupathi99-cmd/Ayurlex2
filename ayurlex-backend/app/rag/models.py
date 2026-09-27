from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from app.models.responses import NormalizedTerm
from app.models.evidence import RetrievedEvidence

class RAGQueryRequest(BaseModel):
    analysis_id: str
    query: str
    innovation_description: Optional[str] = ""
    ingredients: Optional[List[str]] = []
    normalized_terms: Optional[List[NormalizedTerm]] = []
    module: str
    jurisdiction: str
    secondary_jurisdictions: Optional[List[str]] = []
    detected_language: str
    output_language: str
    filters: Optional[Dict[str, Any]] = {}

class QueryAnalysis(BaseModel):
    original_query: str
    normalized_query: str
    detected_language: str
    expanded_terms: List[str]

class RetrievalContext(BaseModel):
    module: str
    primary_jurisdiction: str
    secondary_jurisdictions: List[str]

class RetrievalConfidence(BaseModel):
    score: float
    level: str
    explanation: str

class RAGSystemOutput(BaseModel):
    module: str = "rag_knowledge_system"
    analysis_id: str
    status: str
    query_analysis: QueryAnalysis
    retrieval_context: RetrievalContext
    evidence: List[RetrievedEvidence]
    retrieved_chunks: List[str] = []
    source_metadata: List[Dict[str, Any]] = []
    relevance_scores: List[float] = []
    citation_information: List[Dict[str, str]] = []
    retrieval_limitations: List[str] = []
    retrieval_confidence: RetrievalConfidence
    limitations: List[str]
    metadata: Dict[str, Any]

class DocumentMetadata(BaseModel):
    document_id: str
    title: str
    source: str
    authority: Optional[str] = None
    category: str
    jurisdiction: str
    language: str
    publication_date: Optional[str] = None
    effective_date: Optional[str] = None
    version: Optional[str] = None
    url_reference: Optional[str] = None
    ingestion_date: str

class ChunkMetadata(BaseModel):
    chunk_id: str
    document_id: str
    content: str
    chunk_index: int
    source: str
    authority: Optional[str] = None
    title: str
    language: str
    jurisdiction: str
    category: str
    publication_date: Optional[str] = None
    effective_date: Optional[str] = None
    version: Optional[str] = None
    page: Optional[str] = None
    section: Optional[str] = None
    url_reference: Optional[str] = None
