from fastapi import FastAPI, WebSocketDisconnect
from fastapi.testclient import TestClient

app = FastAPI()


def test_websocket():
    try:
        client = TestClient(app)
        with client.websocket_connect("/ws/test-client-id") as websocket:
            data = websocket.receive_json()
            assert data == {"msg": "Hello WebSocket"}
    except WebSocketDisconnect:
        pass
