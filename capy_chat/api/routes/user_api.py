import uuid

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.user import get_user_by_id
from capy_chat.api.routes.basic_response import BasicResponse

user_router = APIRouter()
logger = get_customized_logger(__name__)


@user_router.get("/user/{user_id}")
async def get_user_info(user_id: str):
    user = get_user_by_id(user_id)
    logger.debug(f"get_user_info: user={user}")
    if user:
        resp = {"status": "OK", "details": {"user": user.to_json()}}
        return JSONResponse(content=resp)
    else:
        resp: BasicResponse = {"status": "ERROR", "details": "User not found"}
        return JSONResponse(status_code=404, content=resp)


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
