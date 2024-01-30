import os
import discord
from discord.ext import commands
from configuration import config

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.queue = []

    @commands.command(pass_context=True)
    async def pause2(self, ctx):
        """Pauses voice of bot

        Args:
            ctx: Controlled Parameter by discord API. Specifies context sent from caller in Discord Server_
        """
        bot_voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if bot_voice.is_playing():
            await ctx.send("Now pausing")
            bot_voice.pause()
        
        else:
            ctx.send(f"{bot_voice} is not playing.")


async def setup(bot):
    await bot.add_cog(Test(bot))