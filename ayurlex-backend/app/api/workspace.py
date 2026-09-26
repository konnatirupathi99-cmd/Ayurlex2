from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import uuid4
from datetime import datetime

from app.models.auth import User
from app.api.auth import require_user
from app.models.workspace import (
    WorkspaceOverview, WorkspaceProject, WorkspaceSession, 
    WorkspaceMessage, WorkspaceReport,
    CreateProjectRequest, CreateSessionRequest, 
    AddMessageRequest, CreateReportRequest,
    ProjectStatus, RoleEnum
)
from app.db.database import DatabaseInterface

router = APIRouter()

@router.get("/overview", response_model=WorkspaceOverview)
async def workspace_overview(user: User = Depends(require_user)):
    """Return the authenticated user's projects, sessions, and reports."""
    user_projects = DatabaseInterface.get_projects_by_user(user.internal_id)
    user_sessions = DatabaseInterface.get_sessions_by_user(user.internal_id)
    user_reports = DatabaseInterface.get_reports_by_user(user.internal_id)
    
    return WorkspaceOverview(
        projects=[WorkspaceProject(**p) for p in user_projects],
        sessions=[WorkspaceSession(**s) for s in user_sessions],
        reports=[WorkspaceReport(**r) for r in user_reports]
    )

@router.get("/sessions/{session_id}/messages", response_model=List[WorkspaceMessage])
async def workspace_messages(session_id: str, user: User = Depends(require_user)):
    """Return messages only for a session owned by the current user."""
    # Check session ownership
    session = DatabaseInterface.get_session(session_id, user.internal_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Session not found or access denied"
        )
        
    session_messages = DatabaseInterface.get_messages_by_session(session_id, user.internal_id)
    return [WorkspaceMessage(
        id=m['id'],
        session_id=m['sessionId'],
        user_id=m['userId'],
        role=RoleEnum(m['role']),
        content=m['content'],
        meta_info=m['meta'],
        citations=m['citations'],
        created_at=m['createdAt']
    ) for m in session_messages]

@router.post("/projects", response_model=WorkspaceProject)
async def create_project(request: CreateProjectRequest, user: User = Depends(require_user)):
    project_dict = DatabaseInterface.create_project(
        id=str(uuid4()),
        user_id=user.internal_id,
        name=request.name,
        description=request.description,
        focus=request.focus,
        primary_jurisdiction=request.primary_jurisdiction
    )
    return WorkspaceProject(**project_dict)

@router.post("/sessions", response_model=WorkspaceSession)
async def create_session(request: CreateSessionRequest, user: User = Depends(require_user)):
    # Verify project ownership
    project = DatabaseInterface.get_project(request.project_id, user.internal_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Project not found or access denied"
        )
        
    session_dict = DatabaseInterface.create_session(
        id=str(uuid4()),
        user_id=user.internal_id,
        project_id=request.project_id,
        title=request.title,
        language=request.language
    )
    return WorkspaceSession(**session_dict)

@router.post("/sessions/{session_id}/messages", response_model=WorkspaceMessage)
async def add_message(session_id: str, request: AddMessageRequest, user: User = Depends(require_user)):
    if session_id != request.session_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session ID mismatch")
        
    # Verify session ownership
    session = DatabaseInterface.get_session(session_id, user.internal_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Session not found or access denied"
        )
        
    msg_dict = DatabaseInterface.add_message(
        id=str(uuid4()),
        user_id=user.internal_id,
        session_id=session_id,
        role=request.role.value,
        content=request.content,
        meta=request.meta_info,
        citations=request.citations
    )
    
    return WorkspaceMessage(
        id=msg_dict['id'],
        session_id=msg_dict['sessionId'],
        user_id=msg_dict['userId'],
        role=RoleEnum(msg_dict['role']),
        content=msg_dict['content'],
        meta_info=msg_dict['meta'],
        citations=msg_dict['citations'],
        created_at=msg_dict['createdAt']
    )

@router.post("/reports", response_model=WorkspaceReport)
async def create_report(request: CreateReportRequest, user: User = Depends(require_user)):
    # Verify project ownership
    project = DatabaseInterface.get_project(request.project_id, user.internal_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Project not found or access denied"
        )
        
    report_dict = DatabaseInterface.create_report(
        id=str(uuid4()),
        user_id=user.internal_id,
        project_id=request.project_id,
        title=request.title,
        report_type=request.report_type,
        payload=request.payload
    )
    return WorkspaceReport(**report_dict)
