from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import jwt
from pydantic import ValidationError
from typing import List, Callable

from app.core import security
from app.db.session import get_db
from app.db.models import User
from app.schemas.auth import TokenPayload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

ROLE_PERMISSIONS = {
    "Administrator": ["knowledge-base management", "document deletion", "admin tools", "system settings", "analytics", "user management", "read", "write"],
    "Practitioner": ["read", "write"],
    "Researcher": ["read", "write", "analytics"],
    "Innovator": ["read", "write"],
    "MSME": ["read", "write"],
    "IP Professional": ["read", "write", "knowledge-base management"],
    "Student": ["read"]
}

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(
            token, security.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = db.query(User).filter(User.id == token_data.sub).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def require_permissions(required_permissions: List[str]) -> Callable:
    def permission_checker(current_user: User = Depends(get_current_active_user)) -> User:
        user_permissions = ROLE_PERMISSIONS.get(current_user.role, [])
        for perm in required_permissions:
            if perm not in user_permissions:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Operation not permitted. Requires {perm} permission.",
                )
        return current_user
    return permission_checker
