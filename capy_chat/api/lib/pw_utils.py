import os
from base64 import b64encode
from hashlib import pbkdf2_hmac


def generate_salt() -> bytes:
    return os.urandom(1024)


def bytes_to_str(input: bytes):
    return b64encode(input).decode("utf-8")


def hash_password(
    plaintext_password: str, salt: bytes = generate_salt(), iterations: int = 210000
) -> str:
    dk: bytes = pbkdf2_hmac(
        "sha512", plaintext_password.encode("ascii"), salt, iterations
    )
    return dk.hex()


def check_password(plaintext_password: str, hashed_password: str, salt: bytes) -> bool:
    return hash_password(plaintext_password, salt) == hashed_password
