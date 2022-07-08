import discord
from discord.utils import get
from discord.ext import commands

class Rooms(commands.Cog):

    def __init__(self, evo):
        self.evo = evo


    # Private rooms main function
    @commands.Cog.listener()
    async def on_voice_state_update(self, member,before,after):
        if after.channel != None: 
            if after.channel.id == 926591934133325886:
                    for guild in self.evo.guilds:
                        maincategory = discord.utils.get(member.guild.categories, id = 789390831957573664)
                        booster=get(member.guild.roles, id=749615132606464071)
                        owner=get(member.guild.roles, id=690297879251648512)
                        if booster in member.roles:
                            channel2 = await guild.create_voice_channel(name = f'💎Комната {member.display_name}',category = maincategory)                            
                            await member.move_to(channel2)
                        if owner in member.roles:
                            channel2 = await guild.create_voice_channel(name = f'🌌Комната {member.display_name}',category = maincategory)                            
                            await member.move_to(channel2)
                        if owner not in member.roles:
                            if booster not in member.roles:
                                channel2 = await guild.create_voice_channel(name = f'🔰Комната {member.display_name}',category = maincategory)                                
                                await member.move_to(channel2)           
                      
                        def check(x,y,z):
                            return len(channel2.members) == 0
                        await self.evo.wait_for('voice_state_update',check=check)
                        await channel2.delete()


def setup(evo):
    evo.add_cog(Rooms(evo))
    print('Rooms loaded')