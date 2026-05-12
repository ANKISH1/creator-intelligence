from fastapi import APIRouter
from app.schemas.chat_request_schema import ChatRequest
from app.databases.storage import storage
from app.services.ai_service import get_answer

router = APIRouter()

@router.post("/chat")
def chat_with_video(chat: ChatRequest):
    transcript = storage.get_transcript(chat.video_id)

    if not transcript:
        return {
            "error":"Transcript not found"
        }
    answer = get_answer(chat.question, transcript)

    return {
        "video_id": chat.video_id,
        "question": chat.question,
        "answer": answer
    }