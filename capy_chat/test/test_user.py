import json
from uuid import uuid4

from fastapi.testclient import TestClient

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.models import User
from capy_chat.api.lib.user import (
    create_user,
    normalize_username,
)
from capy_chat.start_api import app
from capy_chat.test.conftest import create_test_user

client = TestClient(app)
logger = get_customized_logger(__name__)


def test_user_sign_on():
    new_user = create_test_user()
    assert new_user, "Failed to create test user"

    response = client.post(
        "/user/sign-on",
        headers={"Content-Type": "application/json"},
        content=json.dumps(
            {"username": new_user.username, "password": new_user.password}
        ),
    )
    assert response.status_code == 200, "Sign in failed"
    resp_json = response.json()
    assert resp_json["status"] == "OK"
    assert resp_json["details"]["session_id"]


def test_user_info_route():
    uuid = str(uuid4())
    test_user = create_user(uuid, uuid)
    assert isinstance(test_user, User), f"Failed to create test user {uuid}"
    assert test_user.username == uuid
    user_id = test_user.id
    response = client.get(f"/user/{user_id}")
    assert response.status_code == 200, f"Could not find user with ID {user_id}"
    response_json = response.json()

    assert response_json["status"] == "OK"

    user = response_json["details"]["user"]

    assert user, "User not found in response"
    assert user["id"]
    assert user["username"]
    assert user["created_date"]
    assert user["updated_date"]
    assert "active" in user
    assert "password" not in user


def test_user_error():
    response = client.get("/user/asdf")
    assert response.status_code == 404
    resp_json = response.json()
    assert resp_json["details"]
    assert resp_json["status"] == "ERROR"


def test_normalize_username():
    normalized = normalize_username(" TeST      UsErNaMe ")

    assert normalized == "testusername", "Normalization failed"
