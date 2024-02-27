import discord
import random
import youtube_dl
import asyncio
from discord.ext import commands
from cord_dice import cordDice
from cord_util import log

TAG = "main"
PREFIX = '>'

bot = commands.Bot(command_prefix=PREFIX,intents=discord.Intents.all())

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

api_key_file = open('api_key.txt', 'r')
api_key = api_key_file.read()
api_key_file.close()

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
@bot.command(aliases=cordDice.aliases)
async def 주사위(ctx, *vars):
    log.i(TAG, f"{PREFIX}Dice {' '.join(vars)}")
    embed = cordDice.process(vars)
    if embed != -1:
        await ctx.channel.send(embed=embed)
    
bot.run(api_key)