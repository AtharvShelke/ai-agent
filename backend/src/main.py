import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.db import init_db, get_session
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize the database when the app starts."""
    init_db()
    yield
    # Cleanup can be added here if needed


API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise NotImplementedError("API_KEY environment variable is not set.")

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/chat", tags=["chat"])
@app.get("/")

def read_index():
    return {
        "message":"This is a hello message",
        "API_KEY": API_KEY
    }