from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .models import ChatMessage_1Payload, ChatMessage_1, ChatMessage_1Response
from api.db import get_session
from typing import List
router = APIRouter()

@router.get("/")
async def chat():
    return {"message": "Welcome to the chat API!"}


# curl.exe -X GET http://localhost:8080/chat/recent
# This endpoint returns the last 10 messages in the chat
@router.get("/recent", response_model=List[ChatMessage_1Response])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage_1)
    results = session.exec(query).fetchall()[:10]  # Fetch the last 10 messages
    return results


# curl.exe -X POST -d '{\"message\": \"Hello, world!\"}' -H "Content-Type: application/json" http://localhost:8080/chat/
# This endpoint creates a new chat message
@router.post("/", response_model=ChatMessage_1)
def chat_create_message(
    payload:ChatMessage_1Payload,
    session: Session = Depends(get_session)  # Replace with actual session dependency
):
    data = payload.model_dump()
    print(data)

    obj = ChatMessage_1.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)

    return obj