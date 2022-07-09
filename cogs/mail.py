import discord
from discord.ext import commands
from config import MODMAIL_CHANNEL_NAME, LOADED

class Mail(commands.Cog):

    def __init__(self, evo):
        self.evo = evo


    @commands.Cog.listener()
    async def on_message(self, message):
        empty_array = []
        mail_channel = discord.utils.get(self.evo.get_all_channels(), name=MODMAIL_CHANNEL_NAME)

        if message.author == self.evo.user:
            return

        if str(message.channel.type) == "private":
            if message.attachments != empty_array:
                files = message.attachments
                await mail_channel.send("[" + message.author.mention + "]")

                for file in files:
                    await mail_channel.send(file.url)

            else:
                await mail_channel.send("[" + message.author.mention + "] " + message.content)

        elif str(message.channel) == MODMAIL_CHANNEL_NAME and message.content.startswith("<"):
            member_object = message.mentions[0]

            if message.attachments != empty_array:
                files = message.attachments
                await member_object.send("[" + message.author.mention + "]")

                for file in files:
                    await member_object.send(file.url)

            else:
                index = message.content.index(" ")
                string = message.content
                mod_message = string[index:]
                await member_object.send("[" + message.author.mention + "]" + mod_message)
            


def setup(evo):
    evo.add_cog(Mail(evo))
    print(f'Mail {LOADED}')