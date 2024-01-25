import os
import discord
from discord.ext import commands
from configuration import config

class Control(commands.Cog):

    
    def __init__(self, bot):
        self.bot = bot
        self.welcome_message = "Welcome to our server"
    
    @commands.event
    async def on_member_join(self, member):
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"{self.welcome_message} {member}")

    @commands.event
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"{member} has left")

    @commands.event
    async def set_welcome_message(self, ctx):
        self.welcome_message = ctx 
        channel = self.bot.get_channel(config.BOT_CHANNEL)
        await channel.send(f"{self.welcome_message} is now welcome message")


async def setup(bot):
    await bot.add_cog(Control(bot))
        