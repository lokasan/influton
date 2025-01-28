from typing import Optional
from datetime import datetime

from sqlalchemy import BigInteger, Text, DateTime, Boolean, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship

from src.database import Base
from src.users.models import Users


class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Text, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    amount = Column(BigInteger, nullable=False)
    gas = Column(BigInteger, nullable=False)
    network_name = Column(Text, nullable=False)
    token_name = Column(Text, nullable=False)
    is_success = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
