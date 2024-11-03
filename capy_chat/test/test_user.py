import json
import os
from uuid import uuid4

from fastapi.testclient import TestClient
from httpx import Response

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.models import User
from capy_chat.api.lib.user import (
    create_user,
    get_user_by_username, normalize_username,
)
from capy_chat.start_api import app

client = TestClient(app)
logger = get_customized_logger(__name__)


def test_user_sign_on():
    # Create new user
    username = os.urandom(16).hex()
    password = os.urandom(16).hex()
    new_user: User | None = create_user(username, password)

    assert isinstance(new_user, User), "Failed to create test user"
    assert new_user.username
    assert new_user.password

    # Confirm user exists
    db_new_user: User | None = get_user_by_username(new_user.username)
    assert isinstance(db_new_user, User), "Failed to create test user"
    assert db_new_user.username == new_user.username
    assert db_new_user.password == new_user.password

    response: Response = client.post(
        "/user/sign-on",
        headers={"Content-Type": "application/json"},
        content=json.dumps(
            {"username": new_user.username, "password": password}
        ),
    )

    assert response.status_code == 200, "Sign in failed"
    resp_json = response.json()
    assert resp_json["status"] == "OK", "Error signing in"
    assert resp_json["details"]["session_id"]


def test_user_info_route():
    uuid = str(uuid4())
    test_user = create_user(uuid, uuid)
    assert isinstance(test_user, User), f"Failed to create test user {uuid}"
    assert test_user.username == uuid

    response = client.get(f"/user/{test_user.id}")
    assert response.status_code == 200, f"Could not find user with ID {test_user.id}"
    response_json = response.json()

    assert response_json["status"] == "OK"

    user = response_json["details"]["user"]
    assert user, "User not found in response"
    assert user["id"]
    assert user["username"]
    assert user["created_date"]
    assert user["updated_date"]
    assert user["active"]
    assert not user.get("password")


def test_user_error():
    response = client.get("/user/asdf")
    assert response.status_code == 404
    resp_json = response.json()
    assert resp_json["details"]
    assert resp_json["status"] == "ERROR"


def test_normalize_username():
    normalized = normalize_username(" TeST      UsErNaMe ")

    assert normalized == "testusername", "Normalization failed"
