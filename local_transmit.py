import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("> ")
            await websocket.send(message)

if __name__ == "__main__":
    asyncio.run(hello())
