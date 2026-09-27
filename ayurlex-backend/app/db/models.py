import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Boolean, JSON, Integer
from sqlalchemy.orm import relationship
from app.db.session import Base

def generate_uuid():
    return str(uuid.uuid4())

def utc_now():
    return datetime.now(timezone.utc)

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=generate_uuid, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=True) # Nullable for future OAuth users
    role = Column(String, default="Practitioner", nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)
    
    preferences = relationship("UserPreference", back_populates="user", uselist=False)
    conversations = relationship("Conversation", back_populates="user")
    documents = relationship("Document", back_populates="uploader")

class UserPreference(Base):
    __tablename__ = "user_preferences"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), unique=True, index=True)
    preferred_language = Column(String, default="en")
    default_jurisdiction = Column(String, default="International")
    theme = Column(String, default="light")
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    
    user = relationship("User", back_populates="preferences")

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(String, primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    title = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    
    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")
    analyses = relationship("Analysis", back_populates="conversation")

class Message(Base):
    __tablename__ = "messages"
    id = Column(String, primary_key=True, default=generate_uuid)
    conversation_id = Column(String, ForeignKey("conversations.id"), index=True)
    role = Column(String, nullable=False) # 'user', 'assistant', 'system'
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)
    
    conversation = relationship("Conversation", back_populates="messages")
    citations = relationship("Citation", back_populates="message")
    tool_calls = relationship("ToolCall", back_populates="message")

class ToolCall(Base):
    __tablename__ = "tool_calls"
    id = Column(String, primary_key=True, default=generate_uuid)
    message_id = Column(String, ForeignKey("messages.id"), index=True)
    tool_name = Column(String, nullable=False)
    arguments = Column(JSON, nullable=True)
    result = Column(JSON, nullable=True)
    status = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    
    message = relationship("Message", back_populates="tool_calls")

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(String, primary_key=True, default=generate_uuid)
    conversation_id = Column(String, ForeignKey("conversations.id"), nullable=True, index=True)
    title = Column(String, nullable=False)
    analysis_type = Column(String, nullable=False)
    results = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)
    
    conversation = relationship("Conversation", back_populates="analyses")

class Document(Base):
    __tablename__ = "documents"
    id = Column(String, primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    title = Column(String, nullable=False)
    document_type = Column(String, nullable=False)
    category = Column(String, index=True)
    jurisdiction = Column(String, index=True)
    language = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    
    uploader = relationship("User", back_populates="documents")
    versions = relationship("DocumentVersion", back_populates="document")
    chunks = relationship("KnowledgeChunk", back_populates="document")
    source_reference = relationship("Source", back_populates="document", uselist=False)

class DocumentVersion(Base):
    __tablename__ = "document_versions"
    id = Column(String, primary_key=True, default=generate_uuid)
    document_id = Column(String, ForeignKey("documents.id"), index=True)
    version_string = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    changes_summary = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    
    document = relationship("Document", back_populates="versions")

class Source(Base):
    __tablename__ = "sources"
    id = Column(String, primary_key=True, default=generate_uuid)
    document_id = Column(String, ForeignKey("documents.id"), nullable=True, index=True)
    authority = Column(String, nullable=True)
    url = Column(String, nullable=True)
    publication_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    
    document = relationship("Document", back_populates="source_reference")
    citations = relationship("Citation", back_populates="source")

class Citation(Base):
    __tablename__ = "citations"
    id = Column(String, primary_key=True, default=generate_uuid)
    message_id = Column(String, ForeignKey("messages.id"), index=True)
    source_id = Column(String, ForeignKey("sources.id"), index=True)
    snippet = Column(Text, nullable=True)
    relevance_score = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    
    message = relationship("Message", back_populates="citations")
    source = relationship("Source", back_populates="citations")

class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks"
    id = Column(String, primary_key=True, default=generate_uuid)
    document_id = Column(String, ForeignKey("documents.id"), index=True)
    content = Column(Text, nullable=False)
    embedding_id = Column(String, nullable=True) # Reference to vector DB
    page_number = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    
    document = relationship("Document", back_populates="chunks")

class Terminology(Base):
    __tablename__ = "terminology"
    id = Column(String, primary_key=True, default=generate_uuid)
    canonical_term = Column(String, unique=True, index=True)
    sanskrit_form = Column(String, nullable=True)
    scientific_name = Column(String, nullable=True)
    english_equivalent = Column(String, nullable=True)
    variants = Column(JSON, nullable=True) # Store regional variants
    created_at = Column(DateTime(timezone=True), default=utc_now)

class Jurisdiction(Base):
    __tablename__ = "jurisdictions"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True, index=True)
    country_code = Column(String, nullable=False)
    region = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    message_id = Column(String, ForeignKey("messages.id"), nullable=True, index=True)
    rating = Column(Integer, nullable=False) # e.g. 1-5 or -1, 1
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), nullable=True, index=True)
    action = Column(String, nullable=False, index=True)
    resource_type = Column(String, nullable=False)
    resource_id = Column(String, nullable=True)
    details = Column(JSON, nullable=True)
    ip_address = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, index=True)
