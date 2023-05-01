from random import randint
from discord import Embed

def coinflip(ctx):
    coin = randint(0, 1)
    mensagem = f"{ctx.author.mention} "
    if coin == 0:
        mensagem += "**🪙 | Cara!**"
    else:
        mensagem += "**🪙 | Coroa!**"
    embed = Embed(description=mensagem)
    return embed