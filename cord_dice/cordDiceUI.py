import discord
from cord_util import color

def diceEmbedFactory(contents):
    embed = discord.Embed(title=":game_die: 주사위 결과", description=contents, color=color.DEFAULT_VALID_COLOR)
    return embed

def diceErrorEmbedFactory(contents):
    embed = discord.Embed(title=":game_die: Error!", description=contents, color=color.DEFAULT_ERROR_COLOR)
    return embed

def diceHelpEmbedFactory(contents):
    embed = discord.Embed(title=":game_die: 주사위 명령어 사용법", description=contents, color=color.DEFAULT_HELP_COLOR)
    return embed
