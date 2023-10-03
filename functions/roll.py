import discord
from random import randint


def roll(ctx, number):
    """Rola um número x de um dado"""
    if 'd' in str(number):
        numbers = number.split('d')
        if int(numbers[0]) > 500:
            embed = discord.Embed(title=f":game_die: @{ctx.author.name}",
                                  description="O máximo de dados simultâneos é 500.")
            return embed
        results = []
        results_string = "("
        for i in range(0, int(numbers[0])):
            random_num = randint(1, int(numbers[1]))
            results.append(random_num)
            results_string += f"**{str(random_num)}**" if random_num == int(numbers[1]) else str(random_num)
            results_string += ", " if int(numbers[0]) - 1 != i else ""
        results_string += ")"
        embed = discord.Embed(title=f":game_die: @{ctx.author.name}",
                              description=f"**Result:** {number} {results_string}\n**Total:** {sum(results)}")
        return embed
    else:
        r = randint(0, int(number))
        embed = discord.Embed(title=f":game_die: @{ctx.author.name}",
                              description=f"**Result:** 1d{number} ({r})\n**Total:** {r}")
        return embed
