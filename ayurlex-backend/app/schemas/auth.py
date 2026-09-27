from pydantic import BaseModel, EmailStr
from typing import Optional, List

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None
    role: str = "Practitioner" # Practitioner, Researcher, Innovator, MSME, IP Professional, Student, Administrator

class PasswordReset(BaseModel):
    email: EmailStr
    new_password: str

class RoleUpdate(BaseModel):
    role: str
