import discord
from discord.utils import get
from discord.ext import commands
from config import CREATE_ROOM_CHANNEL_ID, LANGUAGE, ROOM_PREFIX, ROOMS_CATEGORY_ID, LOADED, ROOM_NAME

class Rooms(commands.Cog):

    def __init__(self, evo):
        self.evo = evo


    # Private rooms main function
    @commands.Cog.listener()
    async def on_voice_state_update(self, member,before,after):
        if after.channel != None: 
            if after.channel.id == CREATE_ROOM_CHANNEL_ID:
                    for guild in self.evo.guilds:
                        maincategory = discord.utils.get(member.guild.categories, id = ROOMS_CATEGORY_ID)
                        if LANGUAGE == 'EN':
                            channel2 = await guild.create_voice_channel(name = ROOM_PREFIX + member.display_name + ROOM_NAME, category = maincategory)                            
                        if LANGUAGE == 'RU':
                            channel2 = await guild.create_voice_channel(name = ROOM_PREFIX + ROOM_NAME + member.display_name, category = maincategory)   
                        await member.move_to(channel2)        
                      
                        def check(x,y,z):
                            return len(channel2.members) == 0

                        await self.evo.wait_for('voice_state_update',check=check)
                        await channel2.delete()


def setup(evo):
    evo.add_cog(Rooms(evo))
    print(f'Rooms {LOADED}')