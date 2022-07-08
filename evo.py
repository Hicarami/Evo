import os
import discord
from discord.ext import commands


debug = False # Set to True to enable debug mode

if debug == True:
    from dotenv import load_dotenv
    load_dotenv()


# Setting up the bot
TOKEN = os.getenv("EVO_TOKEN")
intents = discord.Intents().all()
evo = commands.Bot(
    command_prefix='.',
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
@evo.command(aliases=['cl'])
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
    evo.load_extension(f'cogs.{extension}')
    await ctx.send(f'```Загружено: {extension}```')

# Unloads the cogs
@evo.command(aliases=['cu'])
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
    evo.unload_extension(f'cogs.{extension}')
    await ctx.send(f'```Выгружено: {extension}```')

# Reloads the cogs
@evo.command(aliases=['cr'])
@commands.has_permissions(administrator = True)
async def reload(ctx, extension):
    evo.reload_extension(f'cogs.{extension}')
    await ctx.send(f'```Перезагружено: {extension}```')


evo.run(TOKEN)