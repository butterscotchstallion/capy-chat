import logging

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from lib import ConnectionManager

manager = ConnectionManager()
ws_router = APIRouter()
logger = logging.getLogger(__file__)


@ws_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    try:
        await manager.connect(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                msg = f"Client #{client_id} says: {data}"
                await manager.send_personal_message(f"You wrote: {data}", websocket)
                await manager.broadcast(msg)
                logger.info(msg)
        except WebSocketDisconnect:
            manager.disconnect(websocket)
            msg = f"Client #{client_id} left the chat"
            await manager.broadcast(msg)
            logger.info(msg)
    except Exception as err:
        logger.error(f"Unexpected error while connecting: {err}")
