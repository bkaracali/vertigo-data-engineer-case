import os
from fastapi import FastAPI
from app.database import engine, Base
from app.models.clan import Clan
from app.routers.clan_router import router as clan_router

try:
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")
except Exception as e:
    print(f"❌ Warning DB init failed: {e}")

app = FastAPI()
app.include_router(clan_router)

@app.get("/")
def health():
    return {"status": "running"}

