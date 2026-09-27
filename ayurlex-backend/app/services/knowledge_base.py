from typing import List, Dict, Any, Optional
from datetime import datetime
from app.models.knowledge_base import KBDocument, KBDocumentVersion, DocumentStatus, KBUploadRequest

class KnowledgeBaseService:
    def __init__(self):
        # In-memory storage for demonstration. In production, use DB.
        self.documents: Dict[str, KBDocument] = {}
        self.versions: Dict[str, List[KBDocumentVersion]] = {}
        
    def upload_document(self, req: KBUploadRequest) -> KBDocument:
        doc = KBDocument(
            title=req.title,
            source=req.source,
            authority=req.authority,
            jurisdiction=req.jurisdiction,
            language=req.language,
            publication_date=req.publication_date,
            effective_date=req.effective_date,
            document_type=req.document_type,
            category=req.category,
            reference_url=req.reference_url,
            content=req.content,
            processing_status=DocumentStatus.PROCESSING
        )
        self.documents[doc.document_id] = doc
        
        # Save initial version
        version = KBDocumentVersion(
            document_id=doc.document_id,
            version=doc.version,
            content=doc.content,
            changes_summary="Initial upload"
        )
        self.versions[doc.document_id] = [version]
        
        return doc
        
    def get_document(self, document_id: str) -> Optional[KBDocument]:
        return self.documents.get(document_id)
        
    def validate_document(self, document_id: str) -> KBDocument:
        doc = self.documents.get(document_id)
        if doc:
            # Add some validation logic here
            pass
        return doc
        
    def extract_document(self, document_id: str) -> KBDocument:
        doc = self.documents.get(document_id)
        if doc:
            # Extract structured data from content
            pass
        return doc

    def index_document(self, document_id: str) -> KBDocument:
        doc = self.documents.get(document_id)
        if doc:
            doc.processing_status = DocumentStatus.INDEXED
            doc.updated_at = datetime.utcnow().isoformat()
        return doc
        
    def reindex_document(self, document_id: str) -> KBDocument:
        doc = self.documents.get(document_id)
        if doc:
            doc.processing_status = DocumentStatus.PROCESSING
            # Mock async processing time, then it would become INDEXED
            doc.updated_at = datetime.utcnow().isoformat()
        return doc
        
    def archive_document(self, document_id: str) -> KBDocument:
        doc = self.documents.get(document_id)
        if doc:
            doc.processing_status = DocumentStatus.ARCHIVED
            doc.updated_at = datetime.utcnow().isoformat()
        return doc
        
    def delete_document(self, document_id: str) -> bool:
        if document_id in self.documents:
            del self.documents[document_id]
            if document_id in self.versions:
                del self.versions[document_id]
            return True
        return False
        
    def search_documents(self, query: str, filters: Optional[Dict[str, Any]] = None) -> List[KBDocument]:
        results = []
        for doc in self.documents.values():
            if doc.processing_status == DocumentStatus.ARCHIVED:
                continue
                
            # Filter logic
            if filters:
                match = True
                for k, v in filters.items():
                    if getattr(doc, k, None) != v:
                        match = False
                        break
                if not match:
                    continue
                    
            # Search logic
            if query.lower() in doc.title.lower() or (doc.content and query.lower() in doc.content.lower()):
                results.append(doc)
                
        return results
        
    def update_document_version(self, document_id: str, new_content: str, changes_summary: str) -> Optional[KBDocument]:
        doc = self.documents.get(document_id)
        if not doc:
            return None
            
        # Increment version
        parts = doc.version.split('.')
        major = int(parts[0]) if len(parts) > 0 else 1
        minor = int(parts[1]) if len(parts) > 1 else 0
        doc.version = f"{major}.{minor + 1}"
        doc.content = new_content
        doc.processing_status = DocumentStatus.UPDATED
        doc.updated_at = datetime.utcnow().isoformat()
        
        # Save version history
        version = KBDocumentVersion(
            document_id=doc.document_id,
            version=doc.version,
            content=doc.content,
            changes_summary=changes_summary
        )
        if document_id not in self.versions:
            self.versions[document_id] = []
        self.versions[document_id].append(version)
        
        return doc
        
    def get_document_history(self, document_id: str) -> List[KBDocumentVersion]:
        return self.versions.get(document_id, [])

kb_service = KnowledgeBaseService()
