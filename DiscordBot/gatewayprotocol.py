from gateway import GatewayCon

class Gateway(GatewayCon):
    async def handle_message(self, msg):
        if msg.op == 10:
            self._pulse = msg.data.hearbeat_interval / 1000
            identity = {

            }
            self.send(identity)

