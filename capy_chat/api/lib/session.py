from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.models import UserSession

from .database import Session

logger = get_customized_logger(__name__)


def get_session_by_id(session_id: str) -> UserSession | None:
    try:
        with Session() as session:
            return (
                session.query(UserSession).filter(UserSession.id == session_id).first()
            )
    except Exception as err:
        logger.error(f"Unexpected error: {err}")


def get_or_create_user_session(user_id: str) -> UserSession | None:
    try:
        user_session = get_session_by_id(user_id)

        if user_session:
            return user_session
        else:
            with Session() as session:
                new_user_session = UserSession(user_id=user_id)
                session.add(new_user_session)
                session.commit()
                return new_user_session
    except Exception as err:
        logger.error(f"Unexpected error: {err}")
