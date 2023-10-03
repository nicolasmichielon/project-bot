from random import randint
from discord import Embed

def coinFlip(ctx):
    """Roda um cara e coroa"""
    coin = randint(0, 1)
    message = f"{ctx.author.mention} "
    if coin == 0:
        message += "**🪙 | Cara!**"
    else:
        message += "**🪙 | Coroa!**"
    embed = Embed(description=message)
    return embed