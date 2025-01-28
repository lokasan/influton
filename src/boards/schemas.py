from pydantic import BaseModel


class BoardContent(BaseModel):
    """Schemas for board content"""
    id: int
    content: str
