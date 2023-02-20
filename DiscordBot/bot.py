from constants import*
from gatewayprotocol import Gateway
from api import DiscordAPI

class Bot(object):
    def __init__(self, token):
        self._g = Gateway(token)
        self.api = DiscordAPI(token)

    def run_gateway(self):
        self.g.run()

    def event(self, f):
        return self.g.event(f)


if __name__ == "__main__":
    token = "foo"
    with open(".token") as token_file:
        token = token_file.read()[:-1]

    bot = Bot("foo")


    @bot.event
    async def message_reaction_add(msg):
        emoji = msg.data.emoji["name"]
        if emoji == "| ? |":
            print("adding announce role")
            user_id = msg.data.user_id
            bot.api.run(f"/guids/{GUILD_ID}/members/{user_id}/roles/{ANNOUNCEMENT_ROLE}", 'PUT')
        else:
            print("skipping misc emoji react")

        bot.run_gateway()
