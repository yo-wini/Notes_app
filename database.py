from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session, declarative_base

DATABASE_URL = "sqlite:///./notesapp.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    with Session(engine) as session:
        yield session
