from fastapi import FastAPI, Request
from app.routes.video_routes import router as video_router
from app.routes.chat_routes import router as chat_router
from app.routes.test import router as test_router
from app.routes.embedding_test import router as test_1_router
from app.databases.db import engine, Base
from app.models.video_model import Video
from app.models.chunk_model import Chunk
import time


app =FastAPI()
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()

    print(f"{request.method} {request.url}")
    print(f"Time Taken: {(end_time - start_time):.3f}")

    return response
 


app.include_router(video_router)
app.include_router(chat_router)
app.include_router(test_router)
app.include_router(test_1_router)

Base.metadata.create_all(bind = engine)

@app.get("/")
def home():
    return {"message": "Backend Running"}