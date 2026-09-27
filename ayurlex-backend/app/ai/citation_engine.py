from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class CitationModel(BaseModel):
    citation_id: str
    document_title: str
    authority: str
    source: str
    jurisdiction: str
    publication_date: str
    page_or_section: str
    relevant_excerpt: str
    reference_url: Optional[str] = None
    relevance_score: float

class ConflictModel(BaseModel):
    topic: str
    description: str
    conflicting_citations: List[str] # List of citation_ids

class CitationEngineOutput(BaseModel):
    citations: List[CitationModel]
    conflicts: List[ConflictModel]
    evidence_status: str # "Found", "Not Found", "Conflicts Detected"

class CitationEngine:
    def format_citations(self, raw_retrieved_evidence: List[Dict[str, Any]]) -> CitationEngineOutput:
        """
        Transforms raw RAG evidence into strict, UI-ready Citation models.
        Detects conflicts if multiple sources disagree on a fundamental attribute.
        """
        if not raw_retrieved_evidence:
            return CitationEngineOutput(
                citations=[],
                conflicts=[],
                evidence_status="No suitable evidence was found to support this query."
            )
            
        citations = []
        for i, ev in enumerate(raw_retrieved_evidence):
            # Safe extraction of metadata fields
            meta = ev.get("metadata", {})
            citations.append(
                CitationModel(
                    citation_id=f"cit_{i+1}",
                    document_title=meta.get("title", "Unknown Document"),
                    authority=meta.get("authority", "Independent"),
                    source=meta.get("source", "Unknown"),
                    jurisdiction=meta.get("jurisdiction", "Unknown"),
                    publication_date=meta.get("publication_date", "N/A"),
                    page_or_section=meta.get("page", "N/A"),
                    relevant_excerpt=ev.get("content", "No excerpt available")[:300] + "...",
                    reference_url=meta.get("url_reference"),
                    relevance_score=ev.get("relevance", ev.get("vector_score", 0.8))
                )
            )
            
        # Conflict Detection (Mocked logical check for demonstration)
        # E.g. If one document says "Approved in India" and another says "Banned in India"
        conflicts = []
        jurisdictions_seen = set()
        for c in citations:
            jurisdictions_seen.add(c.jurisdiction)
            
        if len(jurisdictions_seen) > 1 and len(citations) > 1:
            conflicts.append(
                ConflictModel(
                    topic="Jurisdictional Application",
                    description="Multiple sources disagree on the jurisdictional scope of this regulation. Please review the conflicting evidence.",
                    conflicting_citations=[c.citation_id for c in citations]
                )
            )
            
        status = "Found"
        if conflicts:
            status = "Conflicts Detected"
            
        return CitationEngineOutput(
            citations=citations,
            conflicts=conflicts,
            evidence_status=status
        )

citation_engine = CitationEngine()
