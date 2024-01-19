import os
import discord
from discord.ext import commands
from configuration import config

class Control(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.event
    async def on_member_join(self, member):
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"Welcome {member} to our server")

    @commands.event
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"{member} has left")

async def setup(bot):
    await bot.add_cog(Control(bot))
        