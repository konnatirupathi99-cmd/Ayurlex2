from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import Dict, Any, List, Optional
import os
import tempfile
import uuid
from app.rag.models import RAGQueryRequest, RAGSystemOutput
from app.rag.rag_service import rag_service

router = APIRouter(prefix="/rag")

@router.post("/query", response_model=RAGSystemOutput)
async def query_knowledge(request: RAGQueryRequest):
    try:
        output = rag_service.query(request)
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Retrieval failed: {str(e)}")

@router.post("/ingest")
async def ingest_document(
    file: UploadFile = File(...),
    category: str = Form("General Reference Material"),
    jurisdiction: str = Form("International"),
    source_name: Optional[str] = Form(None)
):
    try:
        # Create a temporary file to save the upload
        fd, temp_path = tempfile.mkstemp(suffix=os.path.splitext(file.filename)[1])
        with os.fdopen(fd, 'wb') as f:
            f.write(await file.read())
            
        metadata = {
            "file_name": file.filename,
            "category": category,
            "jurisdiction": jurisdiction,
            "source_name": source_name or file.filename
        }
        
        result = rag_service.ingest_document(temp_path, metadata)
        
        # Clean up temp file
        os.remove(temp_path)
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")

@router.get("/document/{document_id}")
async def get_document(document_id: str):
    # Stub: Fetch document details from metadata DB
    return {"document_id": document_id, "status": "Not implemented"}

@router.delete("/document/{document_id}")
async def delete_document(document_id: str):
    # Stub: Delete from ChromaDB
    return {"document_id": document_id, "status": "Not implemented"}

@router.get("/status/{analysis_id}")
async def get_rag_status(analysis_id: str):
    # Stub: Fetch async task status
    return {"analysis_id": analysis_id, "status": "completed"}
