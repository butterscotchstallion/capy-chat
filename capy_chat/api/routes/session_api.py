from fastapi import APIRouter
from fastapi.responses import JSONResponse

from capy_chat.api.lib.logger import get_customized_logger
from capy_chat.api.lib.session import get_session_by_id
from capy_chat.api.routes.basic_response import BasicResponse

session_router = APIRouter()

logger = get_customized_logger(__name__)


@session_router.get("/session/{session_id}")
async def session_route(session_id: str):
    """
    Get session info from DB
    """
    try:
        session = get_session_by_id(session_id)
        if session:
            session_info = {"status": "OK", "details": {"session": session.to_json()}}
            return JSONResponse(content=session_info)
        else:
            resp: BasicResponse = {
                "status": "ERROR",
                "details": {"message": "Session not found"},
            }
            return JSONResponse(status_code=404, content=resp)
    except Exception as err:
        logger.error(f"Unexpected error getting session: {err}")
        return JSONResponse(
            content={"status": "ERROR", "message": str(err)}, status_code=500
        )
