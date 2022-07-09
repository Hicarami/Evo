import time
import pytz
import discord
from datetime import datetime
from discord.ext import commands
from config import *

class Mod(commands.Cog):

    def __init__(self, evo):
        self.evo = evo

    # Clear command
    @commands.command(aliases=['clr'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'{amount} {MESSEGES_WERE_DELETED}')
        time.sleep(1)
        await ctx.channel.purge(limit=1)

    # Ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason = reason)
        await ctx.send(f'{USER} {member} {WAS_BANNED_REASON} {reason}')

    # Unban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{USER} {user.mention} {WAS_UNBANNED}')
                return

    # Kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason = reason)
        await ctx.send(f'{USER} {member} {WAS_KICKED_REASON} {reason}')

    # Info command
    @commands.command(aliases=['user','i'])
    @commands.has_permissions(administrator = True)
    async def info(self,ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        emb = discord.Embed(colour = 0x9F85FF)
        emb.set_author(name = f'{INFO_ABOUT} {member}')
        emb.set_thumbnail(url = member.avatar_url)
        emb.set_footer(text = f'{REQUESTED_BY}: {ctx.author}', icon_url = ctx.author.avatar_url)
        emb.add_field(name = f'{NAME_ON_SERVER}:', value = member.display_name)
        emb.add_field(name = f'{ID}:', value = member.id)
        emb.add_field(name = f'{MENTION}:', value = member.mention)

        old_timezone = pytz.timezone("GMT")
        new_timezone = pytz.timezone(PYTZ_TIMEZONE)

        my_timestamp = member.joined_at
        localized_timestamp = old_timezone.localize(my_timestamp)
        new_timezone_timestamp = localized_timestamp.astimezone(new_timezone)
        emb.add_field(name = f'{JOINED}:', value = new_timezone_timestamp.strftime('%x %H:%M:%S'), inline=True)
        s2 = new_timezone_timestamp.strftime('%Y-%m-%d %H:%M:%S')

        my_timestamp = member.created_at
        localized_timestamp = old_timezone.localize(my_timestamp)
        new_timezone_timestamp = localized_timestamp.astimezone(new_timezone)
        emb.add_field(name = f'{ACC_CREATED}:', value = new_timezone_timestamp.strftime("%x %H:%M:%S"), inline=True)

        date = datetime.now(new_timezone)
        s1 = date.strftime('%Y-%m-%d %H:%M:%S')

        fmt = '%Y-%m-%d %H:%M:%S'
        tstamp1 = datetime.strptime(s1, fmt)
        tstamp2 = datetime.strptime(s2, fmt)

        if tstamp1 > tstamp2:
            td = tstamp1 - tstamp2
        else:
            td = tstamp2 - tstamp1

        td_mins = int(round(td.total_seconds() / 60 / 60))
        time = round(td_mins,1)
        emb.add_field(name = BEEN_ON_SERVER, value = f'{time} {HOURS}', inline=True)

        await ctx.send(embed=emb)

    # DM command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dm(self, ctx, user_id=None, *, args=None):
        await ctx.channel.purge(limit = 1)

        if user_id != None and args != None:
            try:
                member = await self.evo.fetch_user(user_id)
                await member.send(args)
                emb3 = discord.Embed(colour = 0x9F85FF)
                emb3.set_author(name=f'{MSG_WAS_SENT} {member.name}')
                emb3.add_field(name=f'{MSG}: `{args}`', value= '** **')
                emb3.set_footer(text=f'{REQUESTED_BY}: {ctx.author}',icon_url=ctx.author.avatar_url)
                await ctx.send(embed=emb3)

            except:
                emb = discord.Embed(colour = 0x9F85FF)
                emb.set_author(name=f'{USER} {NOT_FOUND}')
                await ctx.send(embed=emb)

        else:
            emb2 = discord.Embed(colour = 0x9F85FF)
            emb2.set_author(name=INCORRECT_COMMAND_USAGE)
            emb2.add_field(name=f"{USAGE}:`>dm [{ID}] [{MSG}]`", value= '** **')
            emb2.set_footer(text=f'{REQUESTED_BY}: {ctx.author}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb2)



def setup(evo):
    evo.add_cog(Mod(evo))
    print(f'Mod {LOADED}')