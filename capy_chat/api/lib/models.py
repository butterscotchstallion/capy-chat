from uuid import uuid4

from sqlalchemy import Boolean, DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base
from .logger import get_customized_logger

logger = get_customized_logger(__name__)


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, default=str(uuid4()))
    username: Mapped[str] = mapped_column(String(16))
    password: Mapped[str] = mapped_column(Text)
    salt: Mapped[str] = mapped_column(String(1024))
    created_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    active: Mapped[Boolean] = mapped_column(Boolean(), server_default="t", default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, active={self.active}, created={self.created_date})"
