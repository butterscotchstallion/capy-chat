from fastapi.testclient import TestClient

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.session import get_or_create_user_session
from capy_chat.start_api import app
from capy_chat.test.conftest import create_test_user

client = TestClient(app)
logger = get_customized_logger(__name__)


def test_session_info_route():
    new_user = create_test_user()
    assert new_user, "Failed to create test user"
    user_id = new_user.id
    session_id = get_or_create_user_session(user_id)
    response = client.get(f"/session/{session_id}")
    assert response.status_code == 200, f"Could not find user with ID {user_id}"
