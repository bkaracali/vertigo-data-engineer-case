from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy.orm import Session

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    # Cloud Run default connection format:
    "postgresql+psycopg2://vertigo:vertigo123@/vertigo_db?host=/cloudsql/vertigo-case-488119:europe-central2:vertigo-db-instance"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"options": "-c timezone=UTC"} if "cloudsql" not in DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()