from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum
from datetime import datetime
import uuid

class DocumentStatus(str, Enum):
    PROCESSING = "Processing"
    INDEXED = "Indexed"
    UPDATED = "Updated"
    FAILED = "Failed"
    ARCHIVED = "Archived"

class KBCategory(str, Enum):
    TRADITIONAL_KNOWLEDGE = "Traditional Knowledge"
    AYUSH = "AYUSH"
    INTELLECTUAL_PROPERTY = "Intellectual Property"
    PATENTS = "Patents"
    CDSCO = "CDSCO"
    GEOGRAPHICAL_INDICATIONS = "Geographical Indications"
    WIPO = "WIPO"
    SCIENTIFIC_LITERATURE = "Scientific Literature"
    GOVERNMENT_GUIDELINES = "Government Guidelines"
    INTERNATIONAL_REGULATIONS = "International Regulations"
    AYURVEDA_FORMULATIONS = "Ayurveda formulations"
    REGULATORY_DOCUMENTS = "Regulatory documents"

class KBDocument(BaseModel):
    document_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    source: str
    authority: Optional[str] = None
    jurisdiction: str = "International"
    language: str = "en"
    version: str = "1.0"
    publication_date: Optional[str] = None
    effective_date: Optional[str] = None
    document_type: str
    category: KBCategory
    reference_url: Optional[str] = None
    content: Optional[str] = None
    processing_status: DocumentStatus = DocumentStatus.PROCESSING
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    
class KBDocumentVersion(BaseModel):
    version_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    document_id: str
    version: str
    content: Optional[str] = None
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    changes_summary: Optional[str] = None

class KBSearchRequest(BaseModel):
    query: str
    filters: Optional[Dict[str, Any]] = None
    
class KBUploadRequest(BaseModel):
    title: str
    source: str
    authority: Optional[str] = None
    jurisdiction: str = "International"
    language: str = "en"
    publication_date: Optional[str] = None
    effective_date: Optional[str] = None
    document_type: str
    category: KBCategory
    reference_url: Optional[str] = None
    content: str
