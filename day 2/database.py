# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///tasks.db"  # local SQLite file

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)