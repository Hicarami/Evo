import discord
from discord.ext import commands
from config import LOGGED_AS, LATENCY_IS, LOADED

class Basic(commands.Cog):

    def __init__(self, evo):
        self.evo = evo


    # On ready event
    @commands.Cog.listener()
    async def on_ready(self):
        print("""
                 _______            
                (_______)           
                 _____ _   _ ___    
                |  ___) | | / _ \   
                | |____\ V / |_| |  
                |_______)_/ \___/   
                      by Xhos
        """)
        print(f'{LOGGED_AS} {self.evo.user.name}')
        print(f'{LATENCY_IS} {round(self.evo.latency * 1000)} ms')

    # Ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{LATENCY_IS}: {round(self.evo.latency * 1000)} ms')
        
        

def setup(evo):
    evo.add_cog(Basic(evo))
    print(f'Basic {LOADED}')