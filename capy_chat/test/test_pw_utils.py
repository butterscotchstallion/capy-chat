import os

from capy_chat.api.lib.pw_utils import check_password, generate_password


def test_check_password():
    salt = os.urandom(16)
    plaintext_password = "yumyumyum ice cream so good"
    hashed_password = generate_password(plaintext_password, salt)
    assert check_password(
        plaintext_password, hashed_password, salt
    ), "Password mismatch"
