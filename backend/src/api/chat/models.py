from sqlmodel import SQLModel, Field, DateTime
from datetime import datetime, timezone

def get_utc_now():
    return datetime.now().replace(tzinfo=timezone.utc)

class ChatMessage_1Payload(SQLModel):
    message: str
    

class ChatMessage_1(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    message: str
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=DateTime(timezone=True),
        primary_key=False,
        nullable=False,
    )
    
class ChatMessage_1Response(SQLModel):

    message: str
    created_at: datetime = Field(default=None)


    