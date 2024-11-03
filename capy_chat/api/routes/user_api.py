from base64 import b64decode

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.models import User
from capy_chat.api.lib.pw_utils import check_password
from capy_chat.api.lib.session import get_or_create_user_session
from capy_chat.api.lib.user import get_user_by_id, get_user_by_username
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
        resp: BasicResponse = {
            "status": "ERROR",
            "details": {"message": "User not found"},
        }
        return JSONResponse(status_code=404, content=resp)


@user_router.post("/user/sign-on")
async def user_sign_on(user_info: dict):
    error_resp: BasicResponse = {
        "status": "ERROR",
        "details": {"message": "Invalid username or password"},
    }
    try:
        username: str = user_info["username"]
        password: str = user_info["password"]

        user: User | None = get_user_by_username(username)

        if user:
            logger.debug(f"Authenticating {username}")

            salt_bytes: bytes = b64decode(user.salt, validate=True)
            pw_match: bool = check_password(password, user.password, salt_bytes)
            if pw_match:
                logger.debug(f"Password match for {username}")
                session = get_or_create_user_session(user.id)
                if session:
                    resp_data: BasicResponse = {
                        "status": "OK",
                        "details": {
                            "message": "Session created",
                            "session_id": session.id,
                        },
                    }
                    return JSONResponse(content=jsonable_encoder(resp_data))
                else:
                    logger.error("Error getting user session")
                    server_error_resp: BasicResponse = {
                        "status": "ERROR",
                        "details": {"message": "Server error"},
                    }
                    return JSONResponse(
                        status_code=500, content=jsonable_encoder(server_error_resp)
                    )
            else:
                logger.error(f"Invalid password for {username}")
                return JSONResponse(content=jsonable_encoder(error_resp))
        else:
            logger.error(f"User {username} not found")
            return JSONResponse(status_code=404, content=jsonable_encoder(error_resp))
    except KeyError:
        bad_req_resp: BasicResponse = {
            "status": "ERROR",
            "details": {"message": "Bad request"},
        }
        return JSONResponse(status_code=400, content=jsonable_encoder(bad_req_resp))
    except Exception:
        return JSONResponse(status_code=404, content=jsonable_encoder(error_resp))
