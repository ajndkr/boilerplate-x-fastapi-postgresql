import pytest
from app.models import ChatMessage

def test_create_chat_message():
    message = ChatMessage(text="Hello, world!")
    assert message.text == "Hello, world!"