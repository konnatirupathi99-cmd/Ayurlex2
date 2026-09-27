from fastapi import APIRouter, HTTPException, Query, Body, Path
from typing import List, Dict, Any, Optional
from app.models.knowledge_base import KBDocument, KBDocumentVersion, KBUploadRequest, KBSearchRequest
from app.services.knowledge_base import kb_service

router = APIRouter()

@router.post("/knowledge/upload", response_model=KBDocument)
async def upload_document(request: KBUploadRequest):
    """Upload a new document to the authoritative knowledge base."""
    return kb_service.upload_document(request)

@router.post("/knowledge/{document_id}/validate", response_model=KBDocument)
async def validate_document(document_id: str = Path(...)):
    """Validate document metadata and integrity."""
    doc = kb_service.validate_document(document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.post("/knowledge/{document_id}/extract", response_model=KBDocument)
async def extract_document(document_id: str = Path(...)):
    """Extract structured data and references from document content."""
    doc = kb_service.extract_document(document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.get("/knowledge/{document_id}/preview", response_model=KBDocument)
async def preview_document(document_id: str = Path(...)):
    """Preview document metadata and content."""
    doc = kb_service.get_document(document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.post("/knowledge/{document_id}/index", response_model=KBDocument)
async def index_document(document_id: str = Path(...)):
    """Index the document in the vector store and keyword index."""
    doc = kb_service.index_document(document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.post("/knowledge/{document_id}/reindex", response_model=KBDocument)
async def reindex_document(document_id: str = Path(...)):
    """Re-index a document that has been updated or failed previously."""
    doc = kb_service.reindex_document(document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.post("/knowledge/{document_id}/archive", response_model=KBDocument)
async def archive_document(document_id: str = Path(...)):
    """Archive a document, keeping history but removing from active search."""
    doc = kb_service.archive_document(document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.delete("/knowledge/{document_id}", response_model=Dict[str, Any])
async def delete_document(document_id: str = Path(...)):
    """Permanently delete a document from the system."""
    success = kb_service.delete_document(document_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"status": "success", "message": "Document deleted"}

@router.post("/knowledge/search", response_model=List[KBDocument])
async def search_knowledge(request: KBSearchRequest):
    """Search and filter the authoritative knowledge base."""
    return kb_service.search_documents(request.query, request.filters)

@router.get("/knowledge/{document_id}/history", response_model=List[KBDocumentVersion])
async def get_document_history(document_id: str = Path(...)):
    """Retrieve version history to preserve source provenance and track updates."""
    history = kb_service.get_document_history(document_id)
    if not history:
        raise HTTPException(status_code=404, detail="Document history not found")
    return history

@router.post("/knowledge/{document_id}/update", response_model=KBDocument)
async def update_document_version(
    document_id: str = Path(...), 
    new_content: str = Body(..., embed=True),
    changes_summary: str = Body(..., embed=True)
):
    """Update a document's content and track it as a new version."""
    doc = kb_service.update_document_version(document_id, new_content, changes_summary)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc
