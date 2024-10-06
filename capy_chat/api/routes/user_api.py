import logging
import uuid

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

user_router = APIRouter()
logger = logging.getLogger(__file__)


@user_router.post("/user/sign-on")
async def user_sign_on():
    logger.info("User sign on endpoint")
    # TODO: some actual authentication
    resp_data = {
        "status": "OK",
        "message": "Session created",
        "session_id": uuid.uuid4(),
    }
    return JSONResponse(content=jsonable_encoder(resp_data))
