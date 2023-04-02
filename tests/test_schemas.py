from app.schemas import ChatMessageSchema

def test_chat_message_schema():
    data = {
        "message": "Hello World!",
        "sender": "John Doe",
        "timestamp": "2022-01-01T00:00:00Z"
    }
    schema = ChatMessageSchema()
    result = schema.load(data)
    assert result == data