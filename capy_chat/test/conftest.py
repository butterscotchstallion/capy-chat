import os

from capy_chat.api.lib.models import User
from capy_chat.api.lib.user import create_user


def create_test_user() -> User | None:
    username = os.urandom(16).hex()
    password = os.urandom(16).hex()
    return create_user(username, password)
