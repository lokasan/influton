"""Schemas"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class SUser(BaseModel):
    """Schemas for user"""
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    hash_password: str
    is_active: Optional[bool]
    privilege: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class SUserAuth(BaseModel):
    """Schemas for user register"""
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    username: str
