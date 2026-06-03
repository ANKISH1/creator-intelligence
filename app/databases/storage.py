from app.databases.db import SessionLocal
from app.models.video_model import Video
from app.models.chunk_model import Chunk



class Storage:

    def save_transcript(self,db,video_id, transcript):
        existing_video = db.query(Video).filter(Video.video_id== video_id).first()
        if existing_video:
            return "Transcript already exists"

        new_video = Video(video_id = video_id, transcript = transcript)
        db.add(new_video)
        db.commit()
    

    def get_transcript(self,db,video_id):
        video = db.query(Video).filter(Video.video_id == video_id).first()
        if video:
            return video.transcript
        return None    

    def save_chunks(self,db,video_id,chunks):
        video = db.query(Video).filter(Video.video_id==video_id).first()

        if video is None:
            raise Exception("Video not found")

        for index,text in enumerate(chunks, start=1):
            new_chunk = Chunk(video_id = video.id, chunk_number = index, chunk_text = text)
            db.add(new_chunk)
        db.commit()    

    def get_chunks(self,db,video_id):
        video = db.query(Video).filter(Video.video_id == video_id).first()
        chunks = db.query(Chunk).filter(Chunk.video_id == video.id).all()
        if chunks is None or chunks == []:
            raise Exception("No chunks found")
        return chunks

storage = Storage()