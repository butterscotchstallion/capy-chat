from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_engine(
    "sqlite:///./db.sqlite", connect_args={"check_same_thread": False}
)
Session = sessionmaker(bind=engine, expire_on_commit=False, autoflush=True)
