import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_chat():
    data = {"message": "Hello, World!"}
    response = client.post("/chat", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_chat():
    response = client.get("/chat")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_update_chat():
    data = {"message": "Hello, FastAPI!"}
    response = client.put("/chat", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_delete_chat():
    response = client.delete("/chat")
    assert response.status_code == 200
    assert response.json() == {"message": "Chat deleted."}