from __future__ import annotations

from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base
from .logger import get_customized_logger

logger = get_customized_logger(__name__)


# Child
class UserSession(Base):
    __tablename__ = "user_session"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=str(uuid4()))

    created_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # parent: Mapped["Parent"] = relationship(back_populates="child")
    # parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    user: Mapped["User"] = relationship(back_populates="user_session")
    user_id: Mapped[str] = mapped_column(ForeignKey("user_account.id"))
    UniqueConstraint(user_id)


# Parent
class User(Base):
    __tablename__ = "user_account"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=str(uuid4()))
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

    # child: Mapped["Child"] = relationship(back_populates="parent")
    user_session = relationship(UserSession, back_populates="user", uselist=False)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_date": str(self.created_date),
            "updated_date": str(self.updated_date),
            "active": bool(self.active),
        }

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, active={self.active}, created={self.created_date})"
