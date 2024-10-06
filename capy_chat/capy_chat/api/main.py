from fastapi import FastAPI
from routes.user_api import user_router
from routes.ws_api import ws_router

from capy_chat.capy_chat.api.routes import session_router

app = FastAPI()

app.include_router(ws_router)
app.include_router(user_router)
app.include_router(session_router)
