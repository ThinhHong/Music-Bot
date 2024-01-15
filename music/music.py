import discord
import discord.voice_client
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from configuration import config

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=config.HELP_JOIN)
    async def join(self, ctx):
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
        bot_voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('claire.mp3')
        play = bot_voice.play(source)
        await ctx.send(f"Now playing {music_name}!")

    @commands.command(pass_context=True)
    async def stop(self, ctx):

        bot_voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if bot_voice.is_playing():
            bot_voice.stop()
            await ctx.send("Song has stopped")
            return
        
        await ctx.send("No audo is playing")

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        bot_voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if bot_voice.is_paused():
            await ctx.send("Now resuming")
            bot_voice.resume()
            
        else:
            await ctx.send(f"{bot_voice} is not paused.")  
        
    @commands.command(pass_context=True)
    async def pause(self, ctx):
        bot_voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if bot_voice.is_playing():
            await ctx.send("Now pausing")
            bot_voice.pause()
        
        else:
            ctx.send(f"{bot_voice} is not playing.")

        
    @commands.command(pass_context=True)
    async def toggle(self, ctx):
        bot_voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if bot_voice.is_playing():
            bot_voice.pause()
            await ctx.send("Now pausing")
        else:
            bot_voice.resume()
            await ctx.send("Now resuming")

  

async def setup(bot):
    await bot.add_cog(Music(bot))