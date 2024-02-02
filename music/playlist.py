import discord
import discord.voice_client
import os
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from configuration import config
import random

class Playlist(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.playlist = []
        self.max_length = 20

    @commands.command()
    async def add_playlist(self, ctx, arg: str):
        self.playlist.append(arg)
        await ctx.send(f"Added {arg} to playlist")

    @commands.command()
    async def play_next(self, ctx, arg: str):
        if self.playlist.length > self.max_length:
            await ctx.send("Playlist is full")
            return
            
        self.playlist.append(arg)  
        await ctx.send(f"Added {arg} to playlist")

    @commands.command()
    async def play_random(self, ctx, arg: str):
        random_song = self.playlist[random.randint(0,self.playlist.length)]
        source = FFmpegPCMAudio(random_song)
        bot_voice = ctx.guild.voice_client
        bot_voice.play(source)
        await ctx.send(f"Now playihg {random_song}")

    @commands.command()
    async def remove(self, ctx, arg: str):
        self.playlist.remove(arg)
        await ctx.send(f"Removed {arg} to playlist")

    @commands.command()
    async def show_playlist(self, ctx):
        await ctx.send(self.playlist)

    

async def setup(bot):
    await bot.add_cog(Playlist(bot))