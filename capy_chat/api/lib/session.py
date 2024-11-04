import datetime

from sqlalchemy import func

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.models import UserSession
from .database import Session

logger = get_customized_logger(__name__)


def get_recent_sessions(session_id: str) -> list[UserSession] | None:
    try:
        with Session() as session:
            thirty_days_ago = datetime.datetime.today() - datetime.timedelta(days=30)
            return (
                session.query(UserSession)
                .filter(
                    UserSession.created_date > thirty_days_ago,
                    UserSession.updated_date > thirty_days_ago,
                    UserSession.id == session_id,
                )
                .all()
            )
    except Exception as err:
        logger.error(f"Unexpected error: {err}")


def get_session_by_user_id(user_id: str) -> UserSession | None:
    try:
        with Session() as session:
            return (
                session.query(UserSession).filter(UserSession.user_id == user_id).first()
            )
    except Exception as err:
        logger.error(f"get_session_by_user_id: Unexpected error: {err}")


def get_session_by_id(session_id: str) -> UserSession | None:
    try:
        with Session() as session:
            return (
                session.query(UserSession).filter(UserSession.id == session_id).first()
            )
    except Exception as err:
        logger.error(f"Unexpected error: {err}")


def update_session(session_to_update: UserSession) -> bool:
    try:
        with Session() as session:
            session.add(session_to_update)
            session.commit()
            return True
    except Exception as err:
        logger.error(f"Unexpected error: {err}")
        return False


def get_or_create_user_session(user_id: str) -> UserSession | None:
    try:
        user_session: UserSession | None = get_session_by_user_id(user_id)
        if user_session:
            with Session() as session:
                user_session.updated_date = func.now()
                session.add(user_session)
                session.commit()
                logger.debug(f"Updated existing session for user {user_id}")
                return user_session
        else:
            with Session() as session:
                new_user_session = UserSession(user_id=user_id)
                session.add(new_user_session)
                session.commit()
                logger.debug(f"Created new session for user {user_id}")
                return new_user_session
    except Exception as err:
        logger.error(f"Unexpected error: {err}")
