from fastapi import FastAPI
from app.routes.video_routes import router as video_router
from app.routes.chat_routes import router as chat_router
from app.databases.db import engine, Base
from app.models.video_model import Video

app = FastAPI()
app.include_router(video_router)
app.include_router(chat_router)

Base.metadata.create_all(bind = engine)

@app.get("/")
def home():
    return {"message": "Backend Running"}