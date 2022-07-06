import os
import discord
from dotenv import load_dotenv

load_dotenv()

EvoToken = os.getenv("EvoToken")
AbyssId = os.getenv("AbyssId")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))



client = MyClient()
client.run(EvoToken)