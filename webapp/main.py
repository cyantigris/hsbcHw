import threading

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()


class ConnectionManager:

    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.username_dict: dict[WebSocket, str] = {}
        self.lock = threading.RLock()

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        with self.lock:
            self.active_connections.append(websocket)
            self.username_dict[websocket] = username

    def disconnect(self, websocket: WebSocket):
        with self.lock:
            self.active_connections.remove(websocket)
            del self.username_dict[websocket]

    async def send_single_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, sender: WebSocket):
        for connection in self.active_connections:
            if connection != sender:
                await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{manager.username_dict[websocket]}: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{manager.username_dict[websocket]} has left the chat", websocket)


@app.get("/")
async def get():
    return HTMLResponse(html)


html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="userName" autocomplete="off" placeholder="Enter your username"/>
            <input type="text" id="messageText" autocomplete="off" placeholder="Enter your message"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            const username = prompt("Enter your username:");
            const ws = new WebSocket(`ws://localhost:8000/ws/${username}`);
            ws.onmessage = function(event) {
                const messages = document.getElementById('messages')
                const message = document.createElement('li')
                const content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                const input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
