import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, evo):
        self.evo = evo


    # On ready event
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.evo.user.name}')
        print(f'Latency is {round(self.evo.latency * 1000)} ms')
    

    # Ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Время отклика: {round(self.evo.latency * 1000)} мс')
        
        

def setup(evo):
    evo.add_cog(Basic(evo))
    print('Basic loaded')