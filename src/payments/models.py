from sqlalchemy import Column, BigInteger, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

from src.database import Base


class Payments(Base):
    __tablename__ = 'payments'

    id = Column(BigInteger, primary_key=True)
