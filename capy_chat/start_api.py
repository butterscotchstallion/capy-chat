from fastapi import FastAPI

from capy_chat.api.lib.database import Base, engine
from capy_chat.api.lib.db_setup import create_default_user
from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.routes import session_router, user_router, ws_router

logger = get_customized_logger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="api")

app.include_router(ws_router)
app.include_router(user_router)
app.include_router(session_router)

logger.info("Loaded main API")

create_default_user()
