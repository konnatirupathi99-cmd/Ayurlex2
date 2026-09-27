from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime

class ORMBase(BaseModel):
    class Config:
        from_attributes = True

# --- User & Preferences ---
class UserPreferenceBase(BaseModel):
    preferred_language: str = "en"
    default_jurisdiction: str = "International"
    theme: str = "light"

class UserPreferenceSchema(UserPreferenceBase, ORMBase):
    id: str
    user_id: str
    updated_at: datetime

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserSchema(UserBase, ORMBase):
    id: str
    created_at: datetime
    preferences: Optional[UserPreferenceSchema] = None

# --- Conversations & Messages ---
class ConversationBase(BaseModel):
    title: Optional[str] = None

class ConversationSchema(ConversationBase, ORMBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

class MessageBase(BaseModel):
    role: str
    content: str

class MessageSchema(MessageBase, ORMBase):
    id: str
    conversation_id: str
    created_at: datetime

class ToolCallSchema(ORMBase):
    id: str
    message_id: str
    tool_name: str
    arguments: Optional[Dict[str, Any]]
    result: Optional[Dict[str, Any]]
    status: str
    created_at: datetime

class AnalysisSchema(ORMBase):
    id: str
    conversation_id: Optional[str]
    title: str
    analysis_type: str
    results: Dict[str, Any]
    created_at: datetime

# --- Documents & Knowledge ---
class DocumentVersionSchema(ORMBase):
    id: str
    document_id: str
    version_string: str
    content: str
    changes_summary: Optional[str]
    created_at: datetime

class SourceSchema(ORMBase):
    id: str
    document_id: Optional[str]
    authority: Optional[str]
    url: Optional[str]
    publication_date: Optional[datetime]
    created_at: datetime

class DocumentBase(BaseModel):
    title: str
    document_type: str
    category: Optional[str] = None
    jurisdiction: Optional[str] = None
    language: Optional[str] = None

class DocumentSchema(DocumentBase, ORMBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    source_reference: Optional[SourceSchema] = None
    
class KnowledgeChunkSchema(ORMBase):
    id: str
    document_id: str
    content: str
    embedding_id: Optional[str]
    page_number: Optional[str]
    created_at: datetime

class CitationSchema(ORMBase):
    id: str
    message_id: str
    source_id: str
    snippet: Optional[str]
    relevance_score: Optional[str]
    created_at: datetime

# --- Reference Data ---
class TerminologySchema(ORMBase):
    id: str
    canonical_term: str
    sanskrit_form: Optional[str]
    scientific_name: Optional[str]
    english_equivalent: Optional[str]
    variants: Optional[Dict[str, Any]]
    created_at: datetime

class JurisdictionSchema(ORMBase):
    id: str
    name: str
    country_code: str
    region: Optional[str]
    description: Optional[str]
    created_at: datetime

# --- System ---
class FeedbackSchema(ORMBase):
    id: str
    user_id: str
    message_id: Optional[str]
    rating: int
    comments: Optional[str]
    created_at: datetime

class AuditLogSchema(ORMBase):
    id: str
    user_id: Optional[str]
    action: str
    resource_type: str
    resource_id: Optional[str]
    details: Optional[Dict[str, Any]]
    ip_address: Optional[str]
    created_at: datetime
