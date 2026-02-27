from sqlalchemy.orm import Session
from app.models.clan import Clan
from sqlalchemy import func
from uuid import UUID
from fastapi import HTTPException

def create_clan(db: Session, name: str, region: str):

    existing_clan = db.query(Clan).filter(
        func.lower(Clan.name) == func.lower(name)).first()
    
    if existing_clan:
        raise HTTPException(
            status_code=400, 
            detail=f"Clan with name '{name}' already exists.")

    clan = Clan(name=name, region=region)
    db.add(clan)
    db.commit()
    db.refresh(clan)
    return clan

def get_all_clans(db: Session):
    return db.query(Clan).all()

def search_clan_by_name(db: Session, name: str):
    return db.query(Clan).filter(Clan.name.ilike(f"%{name}%")).all()

def delete_clan(db: Session, clan_id: UUID):
    clan = db.query(Clan).filter(Clan.id == clan_id).first()
    if not clan:
        return None
    db.delete(clan)
    db.commit()
    return clan