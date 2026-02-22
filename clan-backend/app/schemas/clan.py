from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class ClanCreate(BaseModel):
    name: str = Field(..., min_length=3)
    region: str

class ClanResponse(BaseModel):
    id: UUID
    name: str
    region: str
    created_at: datetime

    class Config:
        from_attributes = True