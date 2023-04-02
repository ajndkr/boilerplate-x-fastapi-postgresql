from pydantic import BaseModel

class Message(BaseModel):
    id: int
    sender: str
    content: str

class Chat(BaseModel):
    id: int
    name: str
    messages: list[Message] = []