from sqlalchemy import Column, Integer, Text, ForeignKey

from app.databases.db import Base
from app.models.video_model import Video

class Chunk(Base):
    __tablename__ = "chunks"
    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(Integer, ForeignKey("videos.id"))
    chunk_number = Column(Integer)
    chunk_text = Column(Text)
