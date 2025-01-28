from typing import Optional
from datetime import datetime

from sqlalchemy import Column, BigInteger, Text, DateTime, Boolean, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr

from src.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(Text)
    last_name = Column(Text)
    email = Column(Text, unique=True)
    username = Column(Text, unique=True)
    hash_password = Column(Text)
    is_active = Column(Boolean)
    privilege = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime,  server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime)
