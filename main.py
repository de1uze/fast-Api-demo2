from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os
import logging

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Read port from environment, default to 8000
PORT = int(os.getenv("PORT", "8000"))

app = FastAPI(title="FastAPI assignment", version="1.0.0")

db: dict = {}
counter: int = 0


class Item(BaseModel):
    name: str
    description: Optional[str] = None


# Health check endpoint
@app.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}


@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "hello from pratik, fastAPI working!"}


@app.get("/items")
def list_items():
    logger.info(f"Listing all items — total: {len(db)}")
    return {"items": list(db.values())}


@app.post("/items", status_code=201)
def create_item(item: Item):
    global counter
    counter += 1
    record = {"id": counter, **item.model_dump()}
    db[counter] = record
    logger.info(f"Created item: {item.name} with id: {counter}")
    return record