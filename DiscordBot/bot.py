
class Bot(object):
    def __init__(self, token):
        self._g = Gateway(token)
        self.api = DiscrodAPI(token)

    def run_gateway(self):
        self.g.run()

    def event(self, f):
        return self.g.event(f)

bot = Bot("foo")

@bot.event
async def message_reaction_add(msg):
     bot.api.run(f"/guids/{gid}/members/{user_id}/roles/{role_id}")