from fastapi import APIRouter, Depends
from app.schemas.video_schema import VideoRequest
from app.services.transcript_service import extract_transcript
from app.databases.db import getdb
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/videos")
def process_video(video: VideoRequest, db: Session = Depends(getdb)):

    transcript = extract_transcript(db,video.url)

    return {
        "message": "Video Received, Transcript Extracted",
        "url": video.url,
        "transcript": transcript

    }