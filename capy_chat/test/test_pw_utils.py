from base64 import b64decode

from capy_chat.api.lib.pw_utils import (
    bytes_to_str,
    check_password,
    generate_salt,
    hash_password,
)


def test_check_password():
    salt = generate_salt()
    plaintext_password = "yumyumyum ice cream so good"
    hashed_password = hash_password(plaintext_password, salt)
    assert check_password(
        plaintext_password, hashed_password, salt
    ), "Password mismatch"


def test_db_verify_password():
    plaintext_password = "meowmeow"
    salt_bytes = generate_salt()
    salt_str = bytes_to_str(salt_bytes)
    hashed_password = hash_password(plaintext_password, salt_bytes)
    assert check_password(
        plaintext_password, hashed_password, b64decode(salt_str)
    ), "Verify bytes_to_str failed"
