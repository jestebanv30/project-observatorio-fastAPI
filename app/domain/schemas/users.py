from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    role: str

    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
