import csv
from datetime import datetime, timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.clan import Clan
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://vertigo:vertigo123@db:5432/vertigo_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

CSV_FILE_PATH = "clan_sample_data.csv" 

with open(CSV_FILE_PATH, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Validation: name ve region
        name = row.get("name", "").strip()
        region = row.get("region", "").strip().upper()

        if not name or len(region) != 2:
            print(f"Skipping invalid row: {row}")
            continue

        # created_at parsing
        created_at_raw = row.get("created_at")
        if created_at_raw:
            try:
                # normal datetime format
                created_at = datetime.strptime(created_at_raw, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            except (ValueError, TypeError):
                try:
                    # epoch timestamp
                    created_at = datetime.fromtimestamp(float(created_at_raw), tz=timezone.utc)
                except ValueError:
                    created_at = datetime.now(timezone.utc)
        else:
            created_at = datetime.now(timezone.utc)

        # existing check
        existing = session.query(Clan).filter_by(name=name, region=region).first()
        if existing:
            print(f"Skipping duplicate: {name} / {region}")
            continue

        # add to db
        clan = Clan(name=name, region=region, created_at=created_at)
        session.add(clan)

    session.commit()
    session.close()
    print("Seeding complete!")