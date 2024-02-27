import discord

def diceEmbedFactory(contents):
    embed = discord.Embed(title=":game_die: 주사위 결과", description=contents, color=0x50FF50)
    return embed

def diceErrorEmbedFactory(contents):
    embed = discord.Embed(title=":game_die: Error!", description=contents, color=0xFF5050)
    return embed

def diceHelpEmbedFactory(contents):
    embed = discord.Embed(title=":game_die: 주사위 명령어 사용법", description=contents, color=0x5050FF)
    return embed
