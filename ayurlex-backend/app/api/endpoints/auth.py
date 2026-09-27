from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import verify_password, get_password_hash, create_access_token
from app.core.auth import get_current_active_user
from app.db.session import get_db
from app.db.models import User, UserPreference
from app.schemas.auth import Token, UserCreate, PasswordReset
from app.schemas.database import UserSchema

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", response_model=UserSchema)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    
    hashed_password = get_password_hash(user_in.password)
    new_user = User(
        email=user_in.email,
        name=user_in.name,
        hashed_password=hashed_password,
        role=user_in.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Create default preferences
    new_prefs = UserPreference(user_id=new_user.id)
    db.add(new_prefs)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.post("/login", response_model=Token)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """OAuth2 compatible token login, get an access token for future requests."""
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    # Future compatibility with OAuth users who have no password
    if not user.hashed_password:
        raise HTTPException(status_code=400, detail="Account created via OAuth. Please use Google Login.")
        
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
        
    access_token = create_access_token(subject=user.id)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/reset-password")
def reset_password(reset_in: PasswordReset, db: Session = Depends(get_db)):
    """Reset user password."""
    user = db.query(User).filter(User.email == reset_in.email).first()
    if not user:
        # Prevent email enumeration attacks by returning success even if not found
        return {"msg": "Password reset successful"}
        
    user.hashed_password = get_password_hash(reset_in.new_password)
    db.commit()
    return {"msg": "Password reset successful"}

@router.get("/me", response_model=UserSchema)
def read_user_me(current_user: User = Depends(get_current_active_user)):
    """Get current user profile."""
    return current_user

@router.post("/logout")
def logout():
    """
    Logout is handled client-side by deleting the JWT token.
    For server-side invalidation, a token blacklist could be implemented here.
    """
    return {"msg": "Successfully logged out"}
