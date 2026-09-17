from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

router = APIRouter()

@router.post("/upload")
async def upload_document():
    # Placeholder for document upload (PDF/TXT)
    return {"status": "processing", "document_id": "doc-123"}

@router.get("/")
async def list_documents():
    return {"documents": []}

@router.delete("/{document_id}")
async def delete_document(document_id: str):
    return {"status": "deleted", "document_id": document_id}
