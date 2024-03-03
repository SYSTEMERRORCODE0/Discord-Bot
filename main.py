import discord
import youtube_dl
import asyncio
from discord.ext import commands
from cord_util import log, constants

TAG = "main"

bot = commands.Bot(command_prefix=constants.PREFIX,intents=discord.Intents.all())

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

api_key_file = open('api_key.txt', 'r')
api_key = api_key_file.read()
api_key_file.close()

@bot.event
async def on_ready():
    await bot.load_extension("cord_dice.cordDice")

''' # test on_message
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    
    print(message.content)

    return
'''
'''
@bot.command()
async def help(ctx):
    pass
'''

bot.run(api_key)