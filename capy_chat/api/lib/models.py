from uuid import UUID, uuid4

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base
from .logger import get_customized_logger

logger = get_customized_logger(__name__)


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(String(16))
    password: Mapped[str] = mapped_column(Text)
    salt: Mapped[str] = mapped_column(String(1024))
    # created_date = Column(DateTime, default=datetime.datetime.utcnow) #.now(datetime.timezone.utc)
    created_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username})"
