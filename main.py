from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os


PORT = int(os.getenv("PORT", "8000"))


app = FastAPI(title="FastAPI assignment", version="1.0.0")


db: dict = {}
counter: int = 0

class Item(BaseModel):
    name: str
    description: Optional[str] = None


#New health check endpoint for Task 2
@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")

def root():
    return{"message": "hello from pratik, fastAPI working!"}


@app.get("/items")
def list_items():
    return{"items":list(db.values())}



@app.post("/items", status_code=201)
def create_item(item: Item):
    global counter
    counter += 1
    record = {"id": counter, **item.model_dump()}
    db[counter] = record
    return record
