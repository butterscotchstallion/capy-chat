import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


logger = logging.getLogger(__file__)
engine = create_engine(
    "sqlite:///./db.sqlite", connect_args={"check_same_thread": False}
)

logger.info("Created engine and base")
