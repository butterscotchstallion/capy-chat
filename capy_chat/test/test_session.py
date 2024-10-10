from fastapi.testclient import TestClient

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.models import UserSession
from capy_chat.api.lib.session import get_or_create_user_session
from capy_chat.start_api import app
from capy_chat.test.conftest import create_test_user

client = TestClient(app)
logger = get_customized_logger(__name__)


def test_session_info_route():
    new_user = create_test_user()
    assert new_user, "Failed to create test user"

    user_id = new_user.id
    session = get_or_create_user_session(user_id)
    assert isinstance(session, UserSession), "failed to get session"

    response = client.get(f"/session/{session.id}")
    assert response.status_code == 200, f"Could not find session with ID {user_id}"

    response_json = response.json()
    resp_session = response_json["details"]["session"]
    assert response_json["status"] == "OK"
    assert resp_session["id"]
    assert resp_session["created_date"]
    assert resp_session["updated_date"]


def test_session_error():
    response = client.get("/session/asdf")
    assert response.status_code == 404
    resp_json = response.json()
    assert resp_json["details"]
    assert resp_json["status"] == "ERROR"
