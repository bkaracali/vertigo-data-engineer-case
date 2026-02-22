from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.clan import ClanCreate, ClanResponse
from app.services import clan_service
from typing import List
from uuid import UUID

router = APIRouter(prefix="/clans", tags=["Clans"])

@router.post("/", response_model=ClanResponse)
def create_clan(payload: ClanCreate, db: Session = Depends(get_db)):
    return clan_service.create_clan(db, payload.name, payload.region)

@router.get("/", response_model=List[ClanResponse])
def list_clans(name: str = None, db: Session = Depends(get_db)):
    if name:
        if len(name) < 3:
            raise HTTPException(status_code=400, detail="Name must be at least 3 characters")
        return clan_service.search_clan_by_name(db, name)
    return clan_service.get_all_clans(db)

@router.delete("/{clan_id}")
def delete_clan(clan_id: UUID, db: Session = Depends(get_db)):
    clan = clan_service.delete_clan(db, clan_id)
    if not clan:
        raise HTTPException(status_code=404, detail="Clan not found")
    return {"message": "Clan deleted"}