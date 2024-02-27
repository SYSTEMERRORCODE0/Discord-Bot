'''
This module is for using Dice in discord
'''

import random
from cord_dice import cordDiceUtil
from cord_dice import cordDiceUI

aliases = cordDiceUtil.aliases

def diceRoll(*diceNum):
    print(len(diceNum))
    if len(diceNum) == 1:
        print(diceNum[0], type(diceNum[0]))
        if diceNum[0] <= 0:
            print("fuck")
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
    
    print(errorCode)

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


