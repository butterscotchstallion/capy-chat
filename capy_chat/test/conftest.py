import uuid

from capy_chat.api.lib.models import User
from capy_chat.api.lib.user import create_user


def create_test_user() -> User | None:
    username = str(uuid.uuid4())
    password = username
    return create_user(username, password)
