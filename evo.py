import os
import discord
from discord.ext import commands
from config import DEBUG, DEBUG_IS_ON, PREFIX, LOADED, UNLOADED, RELOADED, LOGING_IN


if DEBUG == True:
    print(DEBUG_IS_ON)
    from dotenv import load_dotenv
    load_dotenv()


# Setting up the bot
TOKEN = os.getenv("EVO_TOKEN")
intents = discord.Intents().all()
evo = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    activity=discord.Streaming(
        name="by Xhos",
        url='https://www.twitch.tv/evodiscord'
        )
    )


# Cogs my beloveds :)

# Loads the cogs on startup
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        evo.load_extension(f'cogs.{filename[:-3]}')

# Loads the cogs
@evo.command()
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
    evo.load_extension(f'cogs.{extension}')
    await ctx.send(f'```{LOADED}: {extension}```')

# Unloads the cogs
@evo.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
    evo.unload_extension(f'cogs.{extension}')
    await ctx.send(f'```{UNLOADED}: {extension}```')

# Reloads the cogs
@evo.command()
@commands.has_permissions(administrator = True)
async def reload(ctx, extension):
    evo.reload_extension(f'cogs.{extension}')
    await ctx.send(f'```{RELOADED}: {extension}```')

print(f'{LOGING_IN}...')

evo.run(TOKEN)