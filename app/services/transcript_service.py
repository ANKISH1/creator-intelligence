from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from app.databases.storage import storage
from app.services.chunking_service import chunkingservice
from app.databases.db import getdb
from sqlalchemy.orm import Session
from fastapi import Depends

def extract_transcript(db,url:str):
    def fetch_video_id(string):
        parsed = urlparse(string)
        query = parse_qs(parsed.query)
        return query.get("v", [None])[0]              

    video_id = fetch_video_id(url)
    existing_transcript = storage.get_transcript(db,video_id)
    if existing_transcript:
        return existing_transcript
    
    else:
        transcript_api = YouTubeTranscriptApi()
        transcript = transcript_api.fetch(video_id, languages=['en', 'hi'])
        final_transcript = " ".join([s.text for s in transcript.snippets])
        storage.save_transcript(db,video_id, final_transcript)
        chunks=chunkingservice.create_chunks(final_transcript)
        storage.save_chunks(db, video_id,chunks)
        return final_transcript