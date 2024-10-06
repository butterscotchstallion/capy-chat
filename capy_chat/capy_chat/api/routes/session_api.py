from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import JSONResponse

session_router = APIRouter()


@session_router.get("/session/{session_id}")
async def session_route(session_id: UUID):
    """
    Get session info from DB
    """
    try:
        pass
    except Exception as err:
        return JSONResponse(
            content={"status": "ERROR", "message": err}, status_code=500
        )
