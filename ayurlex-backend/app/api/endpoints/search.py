from fastapi import APIRouter, Depends
from app.services.search_service import search_engine, SearchFilterRequest, SearchResponse
from app.core.auth import get_current_active_user, require_permissions
from app.db.models import User

router = APIRouter(prefix="/search", tags=["search"])

@router.post("/", response_model=SearchResponse)
async def perform_search(
    query: str,
    filters: SearchFilterRequest = None,
    # Anyone with read permission can search the KB
    current_user: User = Depends(require_permissions(["read"]))
):
    """
    Core AYURLEX Search System.
    Supports Keyword, Semantic, and Hybrid Search.
    Results are strictly reranked by authority and relevance.
    """
    results = search_engine.search(raw_query=query, filters=filters)
    return results
