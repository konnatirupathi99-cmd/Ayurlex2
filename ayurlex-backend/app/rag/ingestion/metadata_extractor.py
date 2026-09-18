import uuid
from datetime import datetime
from typing import Dict, Any
from app.rag.models import DocumentMetadata

class MetadataExtractor:
    """
    Ensures minimum metadata structure is extracted and attached to documents.
    """
    def extract(self, raw_metadata: Dict[str, Any], default_category: str = "General Reference Material", default_jurisdiction: str = "International") -> DocumentMetadata:
        title = raw_metadata.get("title") or raw_metadata.get("file_name") or "Untitled Document"
        
        return DocumentMetadata(
            document_id=str(uuid.uuid4()),
            title=title,
            source_name=raw_metadata.get("source_name", "Unknown Source"),
            source_type=raw_metadata.get("source_type", "Document"),
            category=raw_metadata.get("category", default_category),
            sub_category=raw_metadata.get("sub_category"),
            jurisdiction=raw_metadata.get("jurisdiction", default_jurisdiction),
            jurisdiction_scope=raw_metadata.get("jurisdiction_scope"),
            language=raw_metadata.get("language", "en"),
            publication_date=raw_metadata.get("publication_date"),
            author=raw_metadata.get("author"),
            url=raw_metadata.get("url"),
            version=raw_metadata.get("version"),
            ingestion_date=datetime.utcnow().isoformat() + "Z"
        )
