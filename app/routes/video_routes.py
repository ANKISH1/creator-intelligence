from fastapi import APIRouter
from app.schemas.video_schema import VideoRequest
from app.services.transcript_service import extract_transcript

router = APIRouter()

@router.post("/videos")
def process_video(video: VideoRequest):

    transcript = extract_transcript(video.url)

    return {
        "message": "Video Received, Transcript Extracted",
        "url": video.url,
        "transcript": transcript

    }