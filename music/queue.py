import discord
import discord.voice_client
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from configuration import config
import os

class Queue(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.max_length = 2
        

    @commands.command()
    async def add_queue(self, ctx, song: str):
        if len(self.queue) > self.max_length:
            await ctx.send("Can not add song, The max length of the playlist has been reached")
            return
    
        self.queue.append(song)
        await ctx.send(f"Added {song} to the playlist")


    @commands.command()
    async def play_next(self, ctx):
        music_name = self.queue.pop(0)
        bot_voice = ctx.guild.voice_client
        exist = os.path.isfile(f"./{music_name}")
        source = FFmpegPCMAudio(music_name)

        if not exist:
            await ctx.send(f"{music_name} is not in library")
            return
        
        bot_voice.play(source)
        await ctx.send(f"Now playing {music_name}!")
        
        
    @commands.command()
    async def play_next2(self, ctx):
        music_name = self.queue.pop(0)
        self.play(ctx, music_name)

    @commands.command()  
    async def show_queue(self, ctx):
        await ctx.send(self.queue) 

async def setup(bot):
    await bot.add_cog(Queue(bot))