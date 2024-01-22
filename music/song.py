import discord
import discord.voice_client
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from configuration import config
import queue

class Song(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=config.HELP_JOIN)
    async def join(self, ctx):
        """Function calls bot to enter voice chat user is in
        Failes if user is not in a voice channel

        Args:
            ctx: Controlled Parameter by discord API. Specifies context sent from caller in Discord Server
        """
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
            await ctx.send(f"{self.bot.user.name} has connected to {channel}")
            return

        else:
            await ctx.send(f"{self.bot.user.name} can't join your voice channel since you are not in a channel")
            return

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        """Function forces bot to leave voice chat user is in
        Failes if user is not in a voice channel
        
        Args:
            ctx: Controlled Parameter by discord API. Specifies context sent from caller in Discord Server
        """
        if (ctx.voice_client):
            channel = ctx.message.author.voice.channel
            await ctx.guild.voice_client.disconnect()
            await ctx.send(f"Leaving voice channel {channel}")
            return 
            
        else:
            await ctx.send("Not in voice channel")
            return

    @commands.command(pass_context=True)
    async def play(self, ctx,music_name: str):
        """Playes audio file on computer on voice channel bot is in

        Args:
            ctx: Controlled Parameter by discord API. Specifies context sent from caller in Discord Server_
            music_name (str): name of music user would like to play. Must have file downloaded
        """
        bot_voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(music_name)
        bot_voice.play(source)
        await ctx.send(f"Now playing {music_name}!")

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        """Stops bot's voice in voice channel bot

        Args:
            ctx: Controlled Parameter by discord API. Specifies context sent from caller in Discord Server_
        """

        bot_voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if bot_voice.is_playing():
            bot_voice.stop()
            await ctx.send("Song has stopped")
            return
        
        await ctx.send("No audo is playing")

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        """Resumes voice

        Args:
            ctx: Controlled Parameter by discord API. Specifies context sent from caller in Discord Server_
        """
        bot_voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if bot_voice.is_paused():
            await ctx.send("Now resuming")
            bot_voice.resume()
            
        else:
            await ctx.send(f"{bot_voice} is not paused.")  
        
    @commands.command(pass_context=True)
    async def pause(self, ctx):
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

        
    @commands.command(pass_context=True)
    async def toggle(self, ctx):
        """Toggles bot voice

        Args:
            ctx: Controlled Parameter by discord API. Specifies context sent from caller in Discord Server_
        """
        bot_voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if bot_voice.is_playing():
            bot_voice.pause()
            await ctx.send("Now pausing")
        else:
            bot_voice.resume()
            await ctx.send("Now resuming")

  
async def setup(bot):
    await bot.add_cog(Song(bot))