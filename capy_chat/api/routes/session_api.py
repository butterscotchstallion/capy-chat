from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from capy_chat.api.lib.session import get_session_by_id

session_router = APIRouter()


@session_router.get("/session/{session_id}")
async def session_route(session_id: str):
    """
    Get session info from DB
    """
    try:
        session = get_session_by_id(session_id)
        if session:
            session_info = {"created_date": session.created_date, "user": session.us}
            return JSONResponse(content=session_info)
        else:
            raise HTTPException(404, "Session not found")
    except Exception as err:
        return JSONResponse(
            content={"status": "ERROR", "message": err}, status_code=500
        )
