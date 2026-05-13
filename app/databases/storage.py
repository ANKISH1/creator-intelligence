from app.databases.db import SessionLocal
from app.models.video_model import Video



class Storage:

    def save_transcript(self,video_id, transcript):
        db = SessionLocal()
        existing_video = db.query(Video).filter(Video.video_id== video_id).first()
        if existing_video:
            db.close()
            return "Transcript already exists"

        new_video = Video(video_id = video_id, transcript = transcript)
        db.add(new_video)
        db.commit()
        db.close()
    

    def get_transcript(self,video_id):
        db = SessionLocal()
        video = db.query(Video).filter(Video.video_id == video_id).first()
        db.close()
        if video:
            return video.transcript
        return None        

storage = Storage()