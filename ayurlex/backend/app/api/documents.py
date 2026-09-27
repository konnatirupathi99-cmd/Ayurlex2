import os
import uuid
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from pydantic import BaseModel
from app.rag.chroma_client import get_collection

router = APIRouter()

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "../../../uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

class DocumentResponse(BaseModel):
    id: str
    filename: str
    status: str

@router.post("/documents/upload", response_model=DocumentResponse)
async def upload_document(file: UploadFile = File(...)):
    try:
        doc_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{doc_id}_{file.filename}")
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Basic chunking and indexing for prototype
        collection = get_collection()
        
        # Simulating text extraction (in reality you'd parse PDF/DOCX)
        with open(file_path, "rb") as f:
            content = file.filename + " content simulation"
            
        collection.add(
            documents=[content],
            metadatas=[{"source": file.filename, "jurisdiction": "Unknown"}],
            ids=[doc_id]
        )
            
        return DocumentResponse(
            id=doc_id,
            filename=file.filename,
            status="completed"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
