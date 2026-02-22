from sqlalchemy.orm import Session
from app.models.clan import Clan
from uuid import UUID

def create_clan(db: Session, name: str, region: str):
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