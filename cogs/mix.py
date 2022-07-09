import random
import discord
from discord.ext import commands
from config import EMBED_COLOUR, SUM, DICE, DICE_URL, REQUESTED_BY, RESULT, HEADS, TAILS, FIRST_NUMER, SECOND, BETWEEN, AND, POLL, LOADED

class Mix(commands.Cog):

    def __init__(self, evo):
        self.evo = evo

    # Dice command
    @commands.command(aliases=['d'])
    async def dice(self, ctx):
        n = random.randrange(1,6)
        n2 = random.randrange(1,6)
        n3 = n+n2
        emb = discord.Embed(colour = EMBED_COLOUR)
        emb.set_author(name=f'{SUM}: {n3}')
        emb.add_field(name='** **',value=f'1 {DICE}: **{n}**')
        emb.add_field(name='** **',value=f'2 {DICE} **{n2}**')
        emb.set_thumbnail(url=DICE_URL)
        emb.set_footer(text=f'{REQUESTED_BY}: {ctx.author}',icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    # Coinflip command
    @commands.command(aliases=['coin','c'])
    async def coinflip(ctx):
        n = random.randrange(1,3)
        if n == 1:
            emb2 = discord.Embed(colour = EMBED_COLOUR)
            emb2.set_author(name=f'{RESULT}:')
            emb2.add_field(name=HEADS, value=f'** **')
            emb2.set_thumbnail(url='https://i.imgur.com/y3sZ7Ll.png')
            emb2.set_footer(text=f'{REQUESTED_BY}: {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb2)
        else:
            emb = discord.Embed(colour = EMBED_COLOUR)
            emb.set_author(name=f'{RESULT}:')
            emb.add_field(name=TAILS, value=f'** **')
            emb.set_thumbnail(url='https://i.imgur.com/y3sZ7Ll.png')
            emb.set_footer(text=f'{REQUESTED_BY}: {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)

    # Rand command
    @commands.command(aliases=['r'])
    async def rand(self, ctx,fn:int=None,sn:int=None):
        if fn and sn != None:
            x = fn
            y = sn

        else:
            def check(msg):
                return msg.author == ctx.author and msg.content.isdigit() and msg.channel == ctx.channel

            msg = await ctx.send(f'{FIRST_NUMER}?')
            msg1 = await self.evo.wait_for("message", check=check)
            await msg.edit(content=f'{SECOND}?')
            msg2 = await self.evo.wait_for("message", check=check)
            x = int(msg1.content)
            y = int(msg2.content)

        if x < y:
            value = random.randint(x,y)
            emb = discord.Embed(colour = EMBED_COLOUR)
            emb.set_author(name=f'{RESULT} {value}')
            emb.add_field(name='** **',value=f'{BETWEEN} **{x}** {AND} **{y}**')
            emb.set_thumbnail(url=DICE_URL)
            emb.set_footer(text=f'{REQUESTED_BY}: {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)

        else:
            value = random.randint(y,x)
            emb2 = discord.Embed(colour = EMBED_COLOUR)
            emb2.set_author(name=f'{RESULT} {value}')
            emb2.add_field(name='** **',value=f'{BETWEEN} **{y}** {AND} **{x}**')
            emb2.set_thumbnail(url=DICE_URL)
            emb2.set_footer(text=f'{REQUESTED_BY}: {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb2)

        await msg.delete()
        await msg1.delete()
        await msg2.delete()

    # Poll command
    @commands.command(aliases=['pl'])
    async def poll(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title=POLL,colour = EMBED_COLOUR)
        emb.set_thumbnail(url='https://i.imgur.com/rkRHS7K.png')
        emb.add_field(name='** **', value=f'{message}')
        emb.set_footer(text=f'{REQUESTED_BY}: {ctx.author}',icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')


def setup(evo):
    evo.add_cog(Mix(evo))
    print(f'Mix {LOADED}')