from fastapi import FastAPI
from app.routes.video_routes import router as video_router
from app.routes.chat_routes import router as chat_router

app = FastAPI()
app.include_router(video_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Backend Running"}