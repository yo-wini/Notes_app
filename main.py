from fastapi import FastAPI
from auth.routes import models, router as auth_routes
from auth.notes_routes import router as notes_router
from database import engine
from sqlmodel import SQLModel

app = FastAPI()


app.include_router(auth_routes)
app.include_router(notes_router)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()