from uuid import uuid4

from fastapi.testclient import TestClient

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.models import User
from capy_chat.api.lib.user import (
    create_user,
    normalize_username,
)
from capy_chat.start_api import app

client = TestClient(app)
logger = get_customized_logger(__name__)


def test_user_info_route():
    uuid = str(uuid4())
    test_user = create_user(uuid, uuid)
    assert isinstance(test_user, User), f"Failed to create test user {uuid}"
    assert test_user.username == uuid

    response = client.get(f"/user/{test_user.id}")
    assert response.status_code == 200, response.text


def test_normalize_username():
    normalized = normalize_username(" TeST      UsErNaMe ")

    assert normalized == "testusername", "Normalization failed"
