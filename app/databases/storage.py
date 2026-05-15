from app.databases.db import SessionLocal
from app.models.video_model import Video



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

storage = Storage()