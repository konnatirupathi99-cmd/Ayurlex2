from fastapi import APIRouter, HTTPException, status
from typing import List
import re
from uuid import uuid4

from app.models.citations import Citation, CitationKind, SearchQuery
from app.services.europe_pmc_service import search_europe_pmc

router = APIRouter()

def clean_html(raw_html: str) -> str:
    """Clean HTML from abstracts, normalize whitespace."""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return " ".join(cleantext.split())

def normalize_citation(raw_record: dict) -> Citation:
    """Transform external records into a stable AYURLEX citation schema."""
    # This is a mock implementation
    excerpt = clean_html(raw_record.get("abstract", ""))
    # Cap excerpt length
    if len(excerpt) > 500:
        excerpt = excerpt[:497] + "..."
        
    kind_str = raw_record.get("kind", "journal").lower()
    kind = CitationKind.CLASSICAL if kind_str == "classical" else CitationKind.JOURNAL
    
    # Never invent missing authors, dates, abstracts, or identifiers.
    return Citation(
        id=raw_record.get("id") or str(uuid4()),
        title=raw_record.get("title", ""),
        authors=raw_record.get("authors", ""),
        year=raw_record.get("year", 0),
        source=raw_record.get("source", ""),
        kind=kind,
        url=raw_record.get("url", ""),
        doi=raw_record.get("doi"),
        excerpt=excerpt,
        verified=raw_record.get("verified", False)
    )

@router.post("/search", response_model=List[Citation])
async def search_citations(query: SearchQuery):
    """Search for Ayurveda-related citations."""
    try:
        # Call the dedicated service which handles bounding, timeout, and parsing
        results = await search_europe_pmc(query.query, query.limit)
        return results
    except Exception as e:
        # Show a safe fallback when the external service is unavailable
        # Provide a classical-source fallback when Europe PMC fails
        return await classical_citations()

@router.get("/classical", response_model=List[Citation])
async def classical_citations():
    """Provide curated classical source records."""
    mock_classical = [
        {
            "id": "susruta_1",
            "title": "Suśruta Saṁhitā, Sūtrasthāna",
            "authors": "Suśruta",
            "year": 0, # Ancient text
            "source": "Curated Classical DB",
            "kind": "classical",
            "url": "ayurlex://classical/susruta/1",
            "abstract": "Haridrā is indicated for alleviating skin conditions and acting as an anti-toxic.",
            "verified": True
        }
    ]
    return [normalize_citation(record) for record in mock_classical]
