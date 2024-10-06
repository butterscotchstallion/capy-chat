from fastapi import FastAPI
from lib.database import Base, engine
from lib.logger import get_customized_logger
from lib.models import User
from routes import session_router, user_router, ws_router
from sqlalchemy import select
from sqlalchemy.orm import Session

logger = get_customized_logger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="api")

app.include_router(ws_router)
app.include_router(user_router)
app.include_router(session_router)

logger.info("Loaded main API")

with Session(engine) as session:
    stmt = select(User)
    for user in session.scalars(stmt):
        logger.info(user)
