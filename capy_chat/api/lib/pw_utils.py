import os
from hashlib import pbkdf2_hmac


def hash_password(plaintext_password: str, salt: bytes = os.urandom(1024)) -> str:
    iterations = 210000
    dk = pbkdf2_hmac("sha512", plaintext_password.encode("ascii"), salt, iterations)
    return dk.hex()


def check_password(plaintext_password: str, hashed_password: str, salt: bytes) -> bool:
    return hash_password(plaintext_password, salt) == hashed_password
