from fastapi import APIRouter, Depends, HTTPException, status, Request, Response
from typing import Optional
from datetime import datetime

from app.models.auth import User, UserResponse, AuthStatus

router = APIRouter()

# Mock user database/session management for demonstration
def get_current_user(request: Request) -> Optional[User]:
    # In a real app, verify the session cookie/token here
    session_id = request.cookies.get("ayurlex_session")
    if not session_id:
        return None
    # Mock returning a user
    return User(
        internal_id="usr_123",
        external_open_id="oauth_abc123",
        name="Dr. Researcher",
        email="researcher@example.com",
        login_method="oauth_google",
        role="user",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        last_signin_at=datetime.utcnow()
    )

def require_user(request: Request) -> User:
    """Dependency for protecting private workspace procedures."""
    user = get_current_user(request)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Valid session required"
        )
    return user

def preview_access(request: Request) -> bool:
    """Dependency to permit read-only preview content without exposing private records."""
    # Even if unauthenticated, they can get preview access
    return True

@router.get("/me", response_model=Optional[UserResponse])
async def auth_me(user: Optional[User] = Depends(get_current_user)):
    """Return the current authenticated user or null."""
    if not user:
        return None
    return UserResponse(
        id=user.internal_id,
        name=user.name,
        email=user.email,
        role=user.role
    )

@router.post("/logout", response_model=AuthStatus)
async def auth_logout(response: Response):
    """Clear the session cookie and invalidate the client session."""
    response.delete_cookie(
        "ayurlex_session", 
        secure=True, 
        httponly=True,
        samesite="lax"
    )
    return AuthStatus(status="success", message="Logged out successfully")
