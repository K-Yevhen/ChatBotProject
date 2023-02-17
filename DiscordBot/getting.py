import websockets
import asyncio
from dataclasses import dataclass

GATEWAY_URL = "wss://gateway.discord.gg/"

@dataclass
class GatewayMessage():
    op: int
    data: object
    sequence: int
    name: str


async def run_connection():
    wsurl = f"{GATEWAY_URL}/?v=9&encoding=json"
    async with websockets.connect(wsurl) as ws:
        async for msg in ws:
            print(msg)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_connection())
