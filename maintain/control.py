import os
import discord
from discord.ext import commands
from configuration import config
import sys

sys.path.append(".") # Adds higher directory to python modules path.

class Control(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.welcome_message = "Welcome to our server"
        self.leave_message = "has left"
    
    @commands.event()
    async def on_member_join(self, member):
        """_summary_

        Args:
            member (_type_): _description_
        """
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"{self.welcome_message} {member}")

    @commands.event()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"{member} {self.leave_message}")

    @commands.event()
    async def set_welcome_message(self, ctx):
        self.welcome_message = ctx 
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"{self.welcome_message} is now welcome message")

    @commands.event()
    async def set_leave_message(self, ctx):
        self.leave_message = ctx 
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"{self.leave_message} is now leaving message")


async def setup(bot):
    await bot.add_cog(Control(bot))
        