import discord
from discord.ext import commands
import random
import Joking
from translate import Translator
from functions import clima, ajuda
from functions import news, roll

translator = Translator(to_lang="pt-br")


class gerais(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    intents = discord.Intents.default()
    intents.message_content = True
    comando = commands.Bot(command_prefix='?', intents=intents)

    @comando.command(help="Rola um dado até X valor limite", aliases=("r", "rolls"))
    async def roll(self, ctx, number):
        await ctx.message.delete()
        await ctx.send(embed=roll.roll(ctx, number))

    # command to clear channel messages
    @comando.command(help="Apaga X mensagens do chat")
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @comando.command(help="Conta uma piada")
    async def joke(self, ctx):
        await ctx.send(f"{Joking.random_joke()}")

    @comando.command(help="Ver o clima agora")
    async def weather(self, ctx, *city):
        await ctx.send(clima.climaAgora(city))

    @comando.command(help="Ver o clima nos próximos 5 dias")
    async def forecast(self, ctx, *city):
        await ctx.send(embed=clima.proxClima(city))

    @comando.command(help="Pesquisar uma notícia")
    async def news(self, ctx, *termo):
        await ctx.send(embed=news.searchNews(termo))

    @comando.command(help="Ver todos os comandos")
    async def assist(self, ctx, *mensagem):
        await ctx.send(embed=ajuda.ajuda(mensagem))


async def setup(bot: commands.Bot):
    await bot.add_cog(gerais(bot))
