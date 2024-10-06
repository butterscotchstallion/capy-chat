import json
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import engine
from .logger import get_customized_logger
from .models import User
from .pw_utils import hash_password

logger = get_customized_logger(__name__)


def get_config() -> dict:
    config_text = Path("config.json").read_text()
    return json.loads(config_text)


config = get_config()


def user_exists(username: str) -> bool:
    # TODO: figure out how to make this a count query
    matching_users = []
    with Session(engine) as session:
        stmt = select(User).where(User.username == username)
        for user in session.scalars(stmt):
            matching_users.append(user)
    return len(matching_users) > 0


def create_default_user():
    try:
        if config["default_username"] and config["default_password"]:
            exists = user_exists(config["default_username"])
            if exists:
                logger.debug(f"Default user {config["default_username"]} exists")
            else:
                logger.debug(f"Creating default user {config['default_username']}")

                with Session(engine) as session:
                    default_user = User(
                        username=config["default_username"],
                        password=hash_password(config["default_password"]),
                    )
                    session.add(default_user)
                    session.commit()
                    logger.info(f"Added default user {config["default_user"]}")

    except Exception as err:
        logger.error(f"Error reading config: {err}")
