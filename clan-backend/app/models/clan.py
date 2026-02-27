import uuid
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime, timezone

class Clan(Base):
    __tablename__ = "clans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    region = Column(String, nullable=False)
    created_at = Column(
    DateTime(timezone=True),
    server_default=func.now(),
    nullable=False
    )