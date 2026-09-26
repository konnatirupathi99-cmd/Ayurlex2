from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    internal_id: str
    external_open_id: str
    name: str
    email: EmailStr
    login_method: str
    role: str
    created_at: datetime
    updated_at: datetime
    last_signin_at: datetime

class UserResponse(BaseModel):
    # Safe representation to return to client
    id: str
    name: str
    email: str
    role: str

class AuthStatus(BaseModel):
    status: str
    message: str
