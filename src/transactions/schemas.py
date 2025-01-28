from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class STransaction(BaseModel):
    id: str
    user_id: int
    amount: int
    gas: int
    is_success: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
