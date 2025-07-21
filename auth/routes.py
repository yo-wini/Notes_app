from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlmodel import select
from database import get_db
from auth.models import Note
from auth import models, utils
from pydantic import BaseModel
from auth.utils import decode_access_token
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials


router = APIRouter(prefix="/auth", tags=["Auth"])
security = HTTPBearer()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_pw = utils.hash_password(user.password)
    new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not utils.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = utils.create_access_token({"user_id": db_user.id, "username": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

def get_user_id(token:HTTPAuthorizationCredentials= Depends(security)):
    data = decode_access_token(token.credentials)
    if not data:
        raise HTTPException(status_code=401, detail="Invalid token")
    return data["user_id"]




    
