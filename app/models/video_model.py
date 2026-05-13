from sqlalchemy import Column, Integer, String, Text

from app.databases.db import Base

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String, unique=True, index=True)
    transcript = Column(Text)