import sqlite3
import traceback
from base64 import b64encode

from sqlalchemy import select

from capy_chat.api.lib.models import User
from capy_chat.api.lib.pw_utils import generate_salt, hash_password
from .database import Session
from .logger import get_customized_logger

logger = get_customized_logger(__name__)


def normalize_username(username: str) -> str:
    return username.replace(" ", "").strip().lower()


def get_user_by_username(username: str) -> User | None:
    with Session() as session:
        stmt = select(User).where(User.username == username).limit(1)
        for user in session.scalars(stmt):
            return user


def get_user_by_id(user_id: str) -> User | None:
    user = None
    try:
        with Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
    except Exception as err:
        logger.error(f"Unexpected exception: {err}")
    finally:
        return user


def create_default_user(config: dict) -> User | None:
    return create_user(config["default_username"], config["default_password"])


def create_user(username: str, password: str) -> User | None:
    try:
        exists = get_user_by_username(username)
        if exists:
            logger.debug(f"User {username} exists")
        else:
            with Session() as session:
                random_bytes: bytes = generate_salt()
                salt: str = b64encode(random_bytes).decode("utf-8")
                hashed_password: str = hash_password(password, random_bytes)
                new_user = User(
                    username=username,
                    password=hashed_password,
                    salt=salt,
                )
                session.add(new_user)
                session.commit()
                logger.info(f"Created user {new_user.username}")
                return new_user
    except sqlite3.IntegrityError as integrity_error:
        logger.error(f"Integrity error creating user: {integrity_error}")
    except KeyError as missing_key:
        logger.error(f"Missing key from config: {missing_key}")
    except Exception as err:
        logger.error(f"Error creating user: {err}")
        print(traceback.format_exception(err))
