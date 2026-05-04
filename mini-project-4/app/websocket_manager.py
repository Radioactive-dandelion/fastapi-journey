from fastapi import WebSocket
from typing import Dict, List

class ConnectionManager:
    def __init__(self):
        # poll_id -> list of connections
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, poll_id: str, websocket: WebSocket):
        await websocket.accept()

        if poll_id not in self.active_connections:
            self.active_connections[poll_id] = []

        self.active_connections[poll_id].append(websocket)

    def disconnect(self, poll_id: str, websocket: WebSocket):
        self.active_connections[poll_id].remove(websocket)

        if not self.active_connections[poll_id]:
            del self.active_connections[poll_id]

    async def broadcast(self, poll_id: str, message: dict):
        for connection in self.active_connections.get(poll_id, []):
            await connection.send_json(message)