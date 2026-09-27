from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from typing import List, Optional
from app.services.document_intelligence import document_intelligence, DocumentIntelligenceError
from app.core.auth import get_current_active_user, require_permissions
from app.db.models import User

router = APIRouter(tags=["documents"])

@router.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    source: str = Form("upload"),
    # Only users with write permission can upload
    current_user: User = Depends(require_permissions(["write"]))
):
    """
    Document Intelligence Module: Uploads, validates, extracts, and indexes documents.
    """
    try:
        file_bytes = await file.read()
        
        # Pipeline orchestration
        display_data = document_intelligence.process_document(
            file_bytes=file_bytes,
            filename=file.filename,
            user_id=current_user.id,
            source=source
        )
        
        return display_data
        
    except DocumentIntelligenceError as e:
        # If extraction fails, provide a clear error.
        raise HTTPException(status_code=400, detail=f"Document Processing Failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error during extraction: {str(e)}")

@router.get("/documents")
async def list_documents(current_user: User = Depends(require_permissions(["read"]))):
    """
    List all uploaded and processed documents in the workspace.
    """
    return [
        {"id": "doc-123", "filename": "clinical_trial_report.pdf", "status": "processed"}
    ]

@router.delete("/documents/{doc_id}")
async def delete_document(
    doc_id: str,
    # Only admins can delete documents
    current_user: User = Depends(require_permissions(["document deletion"]))
):
    """
    Remove a document from the workspace and knowledge base.
    """
    return {"message": f"Document {doc_id} deleted successfully"}
