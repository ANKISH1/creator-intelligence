from fastapi import APIRouter, Depends
from app.schemas.video_schema import VideoRequest
from app.services.transcript_service import extract_transcript
from app.databases.db import getdb
from sqlalchemy.orm import Session
from app.databases.storage import storage


router = APIRouter()

@router.get("/chunks")
def get_chunks(db: Session = Depends(getdb)):
    chunks=storage.get_chunks(db,"g-jwWYX7Jlo")
    return chunks    