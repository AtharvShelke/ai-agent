import os

import sqlmodel
from sqlmodel import Session, SQLModel


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise NotImplementedError("DATABASE_URL environment variable is not set.")

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    """Initialize the database."""
    print("Initializing the database...")
    # Create all tables in the database
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:    
        yield session