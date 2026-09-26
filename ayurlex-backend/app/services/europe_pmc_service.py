import re
import urllib.parse
import httpx
import logging
from typing import List, Optional
from uuid import uuid4
from functools import lru_cache

from app.models.citations import Citation, CitationKind
from app.api.system import generate_correlation_id

logger = logging.getLogger(__name__)

# Very basic in-memory caching for deduplication
_CACHE = {}

def clean_html(raw_html: str) -> str:
    """Clean HTML from abstracts, normalize whitespace."""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return " ".join(cleantext.split())

def _build_safe_query(user_query: str) -> str:
    """Combine an Ayurveda term with the user's research terms and URL encode safely."""
    # Ensure it's constrained to Ayurveda literature
    safe_base = user_query.replace('"', '').replace('(', '').replace(')', '')
    combined = f'(ayurveda OR botanical OR traditional medicine) AND ({safe_base})'
    return urllib.parse.quote_plus(combined)

async def search_europe_pmc(query: str, limit: int = 10, timeout: float = 5.0) -> List[Citation]:
    """Search Europe PMC REST API securely on the server side."""
    correlation_id = generate_correlation_id()
    
    # Check cache first
    cache_key = f"{query}_{limit}"
    if cache_key in _CACHE:
        return _CACHE[cache_key]
        
    safe_query_string = _build_safe_query(query)
    
    # Bounded page size
    safe_limit = min(max(limit, 1), 50)
    
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={safe_query_string}&format=json&resultType=core&pageSize={safe_limit}"
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get("resultList", {}).get("result", []):
                # Safely extract and map to AYURLEX citation schema
                epmc_id = item.get("id") or str(uuid4())
                pmcid = item.get("pmcid")
                pmid = item.get("pmid")
                
                # PMCID article URL when available; otherwise a PMID article URL.
                if pmcid:
                    article_url = f"https://europepmc.org/article/PMC/{pmcid}"
                elif pmid:
                    article_url = f"https://europepmc.org/article/MED/{pmid}"
                else:
                    article_url = f"https://europepmc.org/search?query={epmc_id}"

                # Authors
                author_string = item.get("authorString")
                if not author_string:
                    author_string = "Authors unavailable"
                    
                # Year
                pub_year = item.get("pubYear")
                try:
                    pub_year = int(pub_year)
                except (TypeError, ValueError):
                    pub_year = 0 # Fallback
                    
                # Journal source
                journal_title = item.get("journalTitle") or item.get("bookOrReportDetails", {}).get("publisher") or "Unknown Publication"
                source_full = f"{journal_title} (Europe PMC)"
                
                # Excerpt
                raw_abstract = item.get("abstractText", "")
                clean_excerpt = clean_html(raw_abstract)
                if len(clean_excerpt) > 500:
                    clean_excerpt = clean_excerpt[:497] + "..."
                    
                citation = Citation(
                    id=f"epmc_{epmc_id}",
                    title=item.get("title", "Untitled Document"),
                    authors=author_string,
                    year=pub_year,
                    source=source_full,
                    kind=CitationKind.JOURNAL,
                    url=article_url,
                    doi=item.get("doi"),
                    excerpt=clean_excerpt,
                    verified=True
                )
                results.append(citation)
                
            _CACHE[cache_key] = results
            return results
            
    except httpx.RequestError as exc:
        # Log failure without exposing user query content unnecessarily
        logger.error(f"[CORRELATION:{correlation_id}] Europe PMC request failed. Reason: network error.")
        raise
    except Exception as exc:
        logger.error(f"[CORRELATION:{correlation_id}] Europe PMC request failed. Reason: unexpected error.")
        raise
