from fastapi import APIRouter, Depends
from app.schemas.video_schema import VideoRequest
from app.services.transcript_service import extract_transcript
from app.databases.db import getdb
from sqlalchemy.orm import Session
from app.databases.storage import storage
from app.services.embedding_service import embeddingservice
from app.services.embedding_service import model



router = APIRouter()

@router.get("/embedding")
def get_embedding():
    embedding1= embeddingservice.generate_embeddings("I love dogs")
    embedding2 = embeddingservice.generate_embeddings("I love puppies")
    embedding3 = embeddingservice.generate_embeddings("I want to buy a car")

    sim1 = model.similarity(embedding1, embedding2)
    sim2= model.similarity(embedding1, embedding3)


    return {
        "dogs_vs_puppies":sim1,
        "car_vs_dogs": sim2
    }

@router.get("/embedding/similarity")
def get_similarity():
    text1 = "I love dogs"
    text2 = "I like puppies"
    text3 = " I want to buy a car"

    sim1 = embeddingservice.calculate_similarity(text1, text2)
    sim2=  embeddingservice.calculate_similarity(text1, text3)

    return f"dog vs puppies ->{sim1} and dog vs car->{sim2}"