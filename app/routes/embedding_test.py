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

    sim1 = embeddingservice.calculate_similarity_text(text1, text2)
    sim2=  embeddingservice.calculate_similarity_text(text1, text3)

    return f"dog vs puppies ->{sim1} and dog vs car->{sim2}"


@router.get("/retrieve")
def get_chunk(db:Session = Depends(getdb)):
    video_id = "g-jwWYX7Jlo"
    question = "How to build descipline?"
    question_embedding = embeddingservice.generate_embeddings(question)

    chunks = storage.get_chunks(db, video_id=video_id)
    best_chunk = None
    best_similarity = -10
    arr = []

    for chunk in chunks:
        chunk_embedding = embeddingservice.generate_embeddings(chunk.chunk_text)
        similarity = embeddingservice.calculate_similarity_embeddings(chunk_embedding, question_embedding)
        # if similarity.item()> best_similarity:
        #     best_chunk = chunk
        #     best_similarity = similarity.item()
        arr.append({"chunk_number":chunk.chunk_number,
                    "similarity": similarity.item()})

    return arr
        # "Similarity": best_similarity, 
        # "chunk_number": best_chunk.chunk_number, 
        # "chunk_text": best_chunk.chunk_text
