import discord
import discord.voice_client
import os
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from configuration import config
import random

class Song(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.playlist = []
        self.max_length = 20

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
    async def play(self, ctx ,music_name: str):
        """Playes audio file on computer on voice channel bot is in

        Args:
            ctx: Controlled Parameter by discord API. Specifies context sent from caller in Discord Server_
            music_name (str): name of music user would like to play. Must have file downloaded
        """
        bot_voice = ctx.guild.voice_client
        absolute_path = os.path.dirname(__file__)
        print(absolute_path)
        exist = os.path.isfile(f"./{music_name}")
        print(exist)
        source = FFmpegPCMAudio(music_name)
        bot_voice.play(source)
        if not exist:
            await ctx.send(f"{music_name} is not in library")
            return
        
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
        
        await ctx.send("No audio is playing")

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

  

    @commands.command(description=config.HELP_JOIN)
    async def add_queue(self, ctx, song: str):
        if len(self.queue) > self.max_length:
            await ctx.send("Can not add song, The max length of the playlist has been reached")
            return
    
        self.queue.append(song)
        ctx.send(f"Added {song} to the playlist")

    @commands.command(description=config.HELP_JOIN)
    async def play_next(self, ctx):
        song = self.queue.pop(0)
        self.play(ctx, song)
        await ctx.send(f"{song} is now playing")

    @commands.command(description=config.HELP_JOIN)  
    async def shuffle(self, ctx):
        random.shuffle(self.queue)
        await ctx.send("Playlist has been shuffeled")

    @commands.command(description=config.HELP_JOIN)  
    async def show_queue(self, ctx):
        await ctx.send(self.queue) 


async def setup(bot):
    await bot.add_cog(Song(bot))