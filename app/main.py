from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
async def chat():
    return {"message": "Welcome to the chat endpoint!"}