from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel
from auth.models import Note
from auth.utils import decode_access_token
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

router = APIRouter(prefix="/notes", tags=["Notes"])
security = HTTPBearer()

class NoteCreate(BaseModel):
    title:str
    content:str

def get_user_id(token:HTTPAuthorizationCredentials = Depends(security)):
    data = decode_access_token(token.credentials)
    if not data:
        raise HTTPException(status_code=401, detail="Invalid token")
    return data["user_id"]


@router.post("/")
def add_note( note_data: NoteCreate,db: Session = Depends(get_db), user_id: int = Depends(get_user_id)):
    new_note = Note(title=note_data.title, content=note_data.content,user_id=user_id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return {"msg": "Note created", "note": {"id": new_note.id, "title": new_note.title, "content": new_note.content}}

@router.put("/{note_id}")
def update_note(note_id: int,note_data: NoteCreate,   db: Session = Depends(get_db), user_id: int = Depends(get_user_id)):
    note = db.get(Note, note_id)
    if not note or note.user_id != user_id:
        raise HTTPException(status_code=404, detail="Note not found")
    note.title = note_data.title
    note.content = note_data.content
    db.commit()
    return {"msg": "Note updated", "note": {"id": note.id, "title": note.title, "content": note.content}}

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_user_id)):
    note = db.get(Note, note_id)
    if not note or note.user_id != user_id:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"msg": "Note deleted"}
