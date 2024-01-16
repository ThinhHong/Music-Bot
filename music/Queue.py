import discord
import random
import discord.voice_client
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from configuration import config

class Queue(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.max_length = 20

    @commands.command(description=config.HELP_JOIN)
    def enqueue(self, ctx, song: str):
        if len(self.queue) > self.max_length:
            ctx.send("Can not add song, The max length of the playlist has been reached")
            return
    
        self.queue.append(song)
        ctx.send(f"Added {song} to the playlist")

    @commands.command(description=config.HELP_JOIN)
    def dequeue(self, ctx):
        song = self.queue.pop(0)
        ctx.send(f"{song} is now playing")

    @commands.command(description=config.HELP_JOIN)  
    def shuffle(self, ctx):
        random.shuffle(self.queue)
        ctx.send("Playlist has been shuffeled")

    @commands.command(description=config.HELP_JOIN)  
    def show_queue(self, ctx):
        print() 

async def setup(bot):
    await bot.add_cog(Queue(bot))