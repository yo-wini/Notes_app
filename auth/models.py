from sqlalchemy import Column, Integer, String
from database import Base
from sqlmodel import SQLModel,Field
from typing import Optional

class User(SQLModel,table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str


class Note(SQLModel,table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    title:str
    content:str
    user_id:int