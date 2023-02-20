from gateway import GatewayCon

LIB_NAME = 'tmtc-dispy'

class Gateway(GatewayCon):

    def __init__(self, token):
        super().__init__(token)
        self._handlers = {}

    async def handle_message(self, msg):
        print(msg)
        if msg.op == 10:
            print("got HELLO, sending identify")
            self._pulse = msg.data.heartbeat_interval / 1000
            identity = {
                "op": 2,
                "d": {
                    "token": self._token,
                    "intents": 1 << 10,
                    "properties": {
                        "$os": "linux",
                        "$browser": LIB_NAME,
                        "$device": LIB_NAME,
                    },
                }
            }
            await self.send(identity)
            print('done identity')
        elif msg.op == 0:
            event = msg.name.lower()
            if event in self._handlers:
                self._handlers[event](msg)
            else:
                print(f"unhandled event {event}")
        else:
            raise Exception(f"unknown op in message{msg.op}")

if __name__ == "__main__":
    token = "foo"
    with open(".token") as token_file:
        token = token_file.read()[:-1]
        g = Gateway(token)
        g._handlers["ready"] = lambda x: print("ready")
        g.run()
