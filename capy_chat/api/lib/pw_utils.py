import hashlib
import os
from base64 import b64encode


def generate_salt() -> bytes:
    return os.urandom(1024)


def bytes_to_str(input_str: bytes) -> str:
    return b64encode(input_str).decode("utf-8")


def hash_password(
        plaintext_password: str, salt: bytes = generate_salt(), iterations: int = 16384
) -> str:
    block_size: int = 3
    parallelization_factor: int = 2
    return bytes_to_str(
        hashlib.scrypt(
            plaintext_password.encode("utf-8"),
            salt=salt,
            n=iterations,
            r=block_size,
            p=parallelization_factor
        )
    )


def check_password(plaintext_password: str, hashed_password: str, salt: bytes) -> bool:
    return hash_password(plaintext_password, salt) == hashed_password
