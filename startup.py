import os
import discord
from discord.ext import commands
from configuration import config
import configparser
import sys



if __name__ == '__main__':
    absolute_path = os.path.dirname(__file__)
    config_path = "configuration/config.ini"
    config_full_path = os.path.join(absolute_path, config_path)
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(parent_dir)
    #read config file
    config_parser = configparser.ConfigParser()
    try:
        config_parser.read(config_full_path)

    except Exception as e:
            print(f'Could not read configuration file {e}')
            sys.exit()

    bot_token = config_parser['botSetting']['botToken']
    channel_id = int(config.BOT_CHANNEL)
    bot = commands.Bot(command_prefix='!', description=config.BOT_DESCRIPTION, intents=discord.Intents.all())
    bot_extensions = ['music.song','maintain.control','music.test','music.queue']
    
    if bot_token == "":
        print("Error detected, no bot token")
        sys.exit()
    
    
@bot.event
async def on_ready():
    """function has event wrapper. Function runs when bot is activated.
    event wrappers have specific names for specific functions.

    """
    channel = bot.get_channel(channel_id)
    for extension in bot_extensions:
        try:
            await bot.load_extension(extension)
        except Exception as e:
            print(f"Error: {e}")

    await channel.send(f"{bot.user.name} has booted")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

bot.run(bot_token)
