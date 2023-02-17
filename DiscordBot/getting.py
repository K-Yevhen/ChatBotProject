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

class GatewayCon(object):

    def __init__(self, token):
        self.token = token
        self._q = asyncio.Queue()
        self._pulse

    async def _recv_loop(self, ws):
        async for msg in ws:
            await handle_message(msg)

    async def _send_loop(self, ws):
        while True:
            msg = await self._q.get()
            await ws.send(msg)

    async def _ping_loop(self, ws):
        while True:
            asyncio.sleep(self._pulse)
            self._send((
                
    async def handle_message(self, msg):
        pass

    async def _send(self, msg):
       await self._q.put(msg)


async def run_connection():
    wsurl = f"{GATEWAY_URL}/?v=9&encoding=json"
    async with websockets.connect(wsurl) as ws:
        async for msg in ws:
            print(msg)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_connection())
