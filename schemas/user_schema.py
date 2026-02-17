from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
