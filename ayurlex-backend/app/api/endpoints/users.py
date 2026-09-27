from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.auth import require_permissions, get_current_active_user
from app.db.session import get_db
from app.db.models import User
from app.schemas.database import UserSchema
from app.schemas.auth import RoleUpdate

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserSchema])
def get_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    # Only admins or those with user management permission can list users
    current_user: User = Depends(require_permissions(["user management"]))
):
    """Retrieve all users. Requires user management permission."""
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/{user_id}", response_model=UserSchema)
def get_user(
    user_id: str, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_permissions(["user management"]))
):
    """Retrieve a specific user by ID. Requires user management permission."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/{user_id}/role", response_model=UserSchema)
def update_user_role(
    user_id: str, 
    role_update: RoleUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_permissions(["user management"]))
):
    """Update a user's role. Requires user management permission."""
    valid_roles = ["Practitioner", "Researcher", "Innovator", "MSME", "IP Professional", "Student", "Administrator"]
    if role_update.role not in valid_roles:
        raise HTTPException(status_code=400, detail=f"Invalid role. Must be one of: {', '.join(valid_roles)}")
        
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    user.role = role_update.role
    db.commit()
    db.refresh(user)
    return user

@router.patch("/{user_id}/status", response_model=UserSchema)
def toggle_user_status(
    user_id: str, 
    is_active: bool,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_permissions(["user management"]))
):
    """Activate or deactivate a user account. Requires user management permission."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    # Prevent deactivating self
    if user_id == current_user.id and not is_active:
        raise HTTPException(status_code=400, detail="Cannot deactivate your own account")
        
    user.is_active = is_active
    db.commit()
    db.refresh(user)
    return user
