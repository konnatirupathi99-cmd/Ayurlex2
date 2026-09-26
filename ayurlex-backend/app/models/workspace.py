from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
from datetime import datetime
from enum import Enum

class RoleEnum(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"

class ProjectStatus(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"

class WorkspaceProject(BaseModel):
    id: str
    user_id: str
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    focus: str = Field(..., max_length=100)
    primary_jurisdiction: str = Field(..., max_length=100)
    status: ProjectStatus = ProjectStatus.ACTIVE
    created_at: datetime
    updated_at: datetime

class WorkspaceSession(BaseModel):
    id: str
    project_id: str
    user_id: str
    title: str = Field(..., max_length=150)
    language: str = Field(..., max_length=10)
    created_at: datetime
    updated_at: datetime

class WorkspaceMessage(BaseModel):
    id: str
    session_id: str
    user_id: str
    role: RoleEnum
    content: str = Field(..., max_length=5000)
    meta_info: Dict[str, Any] = Field(default_factory=dict)
    citations: List[str] = Field(default_factory=list) # citation IDs
    created_at: datetime

class WorkspaceReport(BaseModel):
    id: str
    project_id: str
    user_id: str
    title: str = Field(..., max_length=150)
    report_type: str = Field(..., max_length=100)
    payload: Dict[str, Any]
    created_at: datetime

class WorkspaceOverview(BaseModel):
    projects: List[WorkspaceProject]
    sessions: List[WorkspaceSession]
    reports: List[WorkspaceReport]

class CreateProjectRequest(BaseModel):
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    focus: str = Field(..., max_length=100)
    primary_jurisdiction: str = Field(..., max_length=100)

class CreateSessionRequest(BaseModel):
    title: str = Field(..., max_length=150)
    language: str = Field(..., max_length=10)
    project_id: str

class AddMessageRequest(BaseModel):
    session_id: str
    role: RoleEnum
    content: str = Field(..., max_length=5000)
    meta_info: Dict[str, Any] = Field(default_factory=dict)
    citations: List[str] = Field(default_factory=list)

class CreateReportRequest(BaseModel):
    title: str = Field(..., max_length=150)
    report_type: str = Field(..., max_length=100)
    payload: Dict[str, Any]
    project_id: str
