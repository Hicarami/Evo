import os
from discord.ext import commands

debug = False

if debug == True:
    from dotenv import load_dotenv
    load_dotenv()

EvoToken = os.getenv("EvoToken")
AbyssId = os.getenv("AbyssId")

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("EvoToken")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command(aliases=['p'])
async def ping(ctx):
    await ctx.send(f'```Время отклика: {round(bot.latency * 1000)} мс```')

if __name__ == "__main__":
    bot.run(TOKEN)