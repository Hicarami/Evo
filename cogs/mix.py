import random
import discord
from discord.ext import commands

class Mix(commands.Cog):

    def __init__(self, evo):
        self.evo = evo

    # Dice command
    @commands.command(aliases=['d'])
    async def dice(self, ctx):
        n = random.randrange(1,6)
        n2 = random.randrange(1,6)
        n3 = n+n2
        emb = discord.Embed(colour = 0x9F85FF)
        emb.set_author(name=f'Сумма {n3}')
        emb.add_field(name='** **',value=f'1 кубик: **{n}**')
        emb.add_field(name='** **',value=f'2 кубик **{n2}**')
        emb.set_thumbnail(url='https://i.imgur.com/HbLQ9CQ.png')
        emb.set_footer(text=f'Запрошено {ctx.author}',icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    # Coinflip command
    @commands.command(aliases=['coin','c'])
    async def coinflip(ctx):
        n = random.randrange(1,3)
        if n == 1:
            emb2 = discord.Embed(colour = 0x9F85FF)
            emb2.set_author(name=f'Результат:')
            emb2.add_field(name=f'Орел',value=f'** **')
            emb2.set_thumbnail(url='https://i.imgur.com/y3sZ7Ll.png')
            emb2.set_footer(text=f'Запрошено {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb2)
        else:
            emb = discord.Embed(colour = 0x9F85FF)
            emb.set_author(name=f'Результат:')
            emb.add_field(name=f'Решка',value=f'** **')
            emb.set_thumbnail(url='https://i.imgur.com/y3sZ7Ll.png')
            emb.set_footer(text=f'Запрошено {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)

    # Rand command
    @commands.command(aliases=['rand'])
    async def r(self, ctx,fn:int=None,sn:int=None):
        if fn and sn != None:
            x = fn
            y = sn
            print('123')
        else:
            def check(msg):
                return msg.author == ctx.author and msg.content.isdigit() and \
                    msg.channel == ctx.channel
            msg = await ctx.send("Первое число?")
            msg1 = await self.evo.wait_for("message", check=check)
            await msg.edit(content="Второе?")
            msg2 = await self.evo.wait_for("message", check=check)
            x = int(msg1.content)
            y = int(msg2.content)
        if x < y:
            value = random.randint(x,y)
            emb = discord.Embed(colour = 0x9F85FF)
            emb.set_author(name=f'Выпало {value}')
            emb.add_field(name='** **',value=f'Между **{x}** и **{y}**')
            emb.set_thumbnail(url='https://i.imgur.com/HbLQ9CQ.png')
            emb.set_footer(text=f'Запрошено {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)
        else:
            value = random.randint(y,x)
            emb2 = discord.Embed(colour = 0x9F85FF)
            emb2.set_author(name=f'Выпало {value}')
            emb2.add_field(name='** **',value=f'Между **{y}** и **{x}**')
            emb2.set_thumbnail(url='https://i.imgur.com **{y}** и **{x}**')
            emb2.set_thumbnail(url='https://i.imgur.com/HbLQ9CQ.png')
            emb2.set_footer(text=f'Запрошено {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb2)
        await msg.delete()
        await msg1.delete()
        await msg2.delete()

    # Poll command
    @commands.command(aliases=['pl'])
    async def poll(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title="Голосование",colour = 0x9F85FF)
        emb.set_thumbnail(url='https://i.imgur.com/rkRHS7K.png')
        emb.add_field(name='** **', value=f'{message}')
        emb.set_footer(text=f'Голосование начал: {ctx.author}',icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')


def setup(evo):
    evo.add_cog(Mix(evo))
    print('Mix loaded')