from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
async def get_chat():
    return {"message": "Welcome to the chat endpoint!"}

@router.post("/chat")
async def post_chat():
    return {"message": "Message sent to the chat!"}