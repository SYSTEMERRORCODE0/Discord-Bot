'''
This module is for using Dice in discord
'''

import random
from discord.ext import commands
from cord_dice import cordDiceUtil
from cord_dice import cordDiceUI
from cord_util import log, constants

TAG = "cordDice"

@commands.command(aliases=cordDiceUtil.aliases)
async def 주사위(ctx, *vars):
    log.i(TAG, f"{constants.PREFIX}Dice {' '.join(vars)}")
    embed = process(vars)
    if embed != -1:
        await ctx.channel.send(embed=embed)

def diceRoll(*diceNum):
    if len(diceNum) == 1:
        if diceNum[0] <= 0:
            return cordDiceUtil.ERROR_ONE_INVALID_ARGUMENT
        n = random.randrange(1, diceNum[0] + 1)
    else:
        if diceNum[0] > diceNum[1]:
            return cordDiceUtil.ERROR_TWO_INVALID_ARGUMENT
        n = random.randrange(diceNum[0], diceNum[1] + 1)
    return n


def process(vars):

    errorCode = cordDiceUtil.ERROR_NOT_DEFINED

    if len(vars) == 0 or vars[0] == "help":
        errorCode = cordDiceUtil.ERROR_HELP
    
    elif len(vars) == 1:
        try:
            n = int(vars[0])
            errorCode = diceRoll(n)
        except:
            pass
    
    else:
        try:
            n = int(vars[0])
            m = int(vars[1])
            errorCode = diceRoll(n, m)
        except:
            pass
    
    log.i(TAG, errorCode)

    return diceEmbedding(errorCode)



def diceEmbedding(errorCode):
    match(errorCode):
        case cordDiceUtil.ERROR_NOT_DEFINED:
            return -1
        case cordDiceUtil.ERROR_ONE_INVALID_ARGUMENT:
            return cordDiceUI.diceErrorEmbedFactory(cordDiceUtil.one_argument_help)
        case cordDiceUtil.ERROR_TWO_INVALID_ARGUMENT:
            return cordDiceUI.diceErrorEmbedFactory(cordDiceUtil.two_argument_help)
        case cordDiceUtil.ERROR_HELP:
            return cordDiceUI.diceHelpEmbedFactory(cordDiceUtil.help)
        case _:
            return cordDiceUI.diceEmbedFactory(str(errorCode))


async def setup(bot):
    bot.add_command(주사위)