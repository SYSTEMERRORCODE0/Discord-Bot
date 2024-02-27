import discord
import random
import youtube_dl
import asyncio
from discord.ext import commands
from cord_dice import cordDice

bot = commands.Bot(command_prefix='>',intents=discord.Intents.all())

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

api_key_file = open('api_key.txt', 'r')
api_key = api_key_file.read()
api_key_file.close()

''' test on_message
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    
    print(message.content)
    await message.channel.send('Received message')
    return
'''
'''
@bot.command()
async def help(message):
    pass
'''
@bot.command(aliases=cordDice.aliases)
async def 주사위(message, *vars):
    embed = cordDice.process(vars)
    if embed != -1:
        await message.channel.send(embed=embed)
    
bot.run(api_key)