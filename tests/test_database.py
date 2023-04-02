import pytest
from app.database import get_db


def test_get_db():
    with pytest.raises(RuntimeError):
        db = get_db()
        assert db is None