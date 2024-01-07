import configparser
import discord
from discord.ext import commands, tasks
import sys

#read config file
config = configparser.ConfigParser()
try:
    config.read('configbot.ini')

except Exception as e:
        print(f'Could not read configuration file {e}')
        sys.exit()

bot_token = config['botSetting']['botToken']
channel_id = int(config['botSetting']['channelId'])

bot_description = "This bot is designed to play music in any discord channel. As well as queing and"

#intents are neccesary for a bot to function. They are choosen by a user
#Each attribute in the Intents class documents which events a bot can corresponds to and which caches it enables.
intents = discord.Intents.all()

intents.message_content = True

bot = commands.Bot(command_prefix='!', description=bot_description, intents=intents)

