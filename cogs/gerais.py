import discord
from discord.ext import commands
import random
import Joking
from translate import Translator
from functions import clima

translator = Translator(to_lang="pt-br")


class gerais(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    intents = discord.Intents.default()
    intents.message_content = True
    comando = commands.Bot(command_prefix='!', intents=intents)

    @comando.command(help="Rola um dado até X valor limite")
    async def roll(self, ctx, number):
        await ctx.channel.purge(limit=1)
        r = random.randint(0, int(number))
        await ctx.send(f"🎲 {ctx.author.mention}\n {r}")

    # command to clear channel messages
    @comando.command(help="Apaga X mensagens do chat")
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @comando.command(help="Conta uma piada")
    async def piada(self, ctx):
        await ctx.send(f"{translator.translate(Joking.random_joke())}")

    @comando.command(help="Ver o clima agora")
    async def clima(self, ctx):
        await ctx.send(clima.climaAgora())


async def setup(bot: commands.Bot):
    await bot.add_cog(gerais(bot))
