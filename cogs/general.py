import Joking
import discord
from discord.ext import commands
from translate import Translator
from functions import coinToday, pokemon
from functions import roll, gifs, coinFlip
from functions.clashRoyale import clashroyale
from functions.media import news, weather, movie

translator = Translator(to_lang="pt-br")

class Gerais(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    intents = discord.Intents.default()
    intents.message_content = True
    comando = commands.Bot(command_prefix="?", intents=intents,help_command=None)

    @comando.command(help="Rola um dado até X valor limite", aliases=("r", "rolls"))
    async def roll(self, ctx, number):
        await ctx.message.delete()
        await ctx.send(embed=roll.roll(ctx, number))

    @comando.command(help="Apaga X mensagens do chat")
    async def clear(self, ctx, amount=5 ):
        await ctx.channel.purge(limit=amount)

    @comando.hybrid_command(help="Conta uma piada")
    async def joke(self, ctx):
        await ctx.send(f"{Joking.DarkJoke()}")

    @comando.command(help="Ver o clima agora")
    async def weather(self, ctx, *city):
        await ctx.send(weather.weather(city))

    @comando.command(help="Pesquisa um filme")
    async def searchmovie(self, ctx,*movie_name):
        await ctx.send(embed=movie.searchMovie(movie_name))
    @comando.command(help="Ver o clima nos próximos 5 dias")
    async def forecast(self, ctx, *city):
        await ctx.send(embed=weather.forecast(city))

    @comando.command(help="Pesquisar uma notícia")
    async def news(self, ctx):
        await news.searchNews(ctx)


    @comando.command(help="Ver o valor do real")
    async def real(self, ctx):
        await ctx.send(embed=coinToday.realToday())
    @comando.command(help="Ver o valor do dólar")
    async def dollar(self, ctx):
        await ctx.send(embed=coinToday.dollarToday())

    @comando.command(help="Cara ou coroa")
    async def coinflip(self, ctx):
        await ctx.send(embed=coinFlip.coinFlip(ctx))

    @comando.command(help="Procura um gif")
    async def gif(self, ctx, *termo):
        await ctx.send(gifs.gifSearch(termo))
     
    @comando.command(help="confsoundboardigura um clan no Clash Royale")
    async def setclanCR(self, ctx, *clan):
        await ctx.send(embed=await clashroyale.setClanRoyale(clan,ctx.guild,ctx))
    @comando.command(help="Pesquisa um clan através da tag")
    async def searchClanCR(self, ctx, *clan):
        await ctx.send(embed= clashroyale.searchClanRoyale(clan))
    @comando.command(help="Da um tapa")
    async def slap(self, ctx, user):
        await ctx.send(embed=gifs.slap(ctx, user))

    @comando.command(help="Beija alguém")
    async def kiss(self, ctx, user):
        await ctx.send(embed=gifs.kiss(ctx, user))

    @comando.command(help="Soca alguém")
    async def punch(self, ctx, user):
        await ctx.send(embed=gifs.punch(ctx, user))

    @comando.command(help="Abraça alguém")
    async def hug(self, ctx, user):
        await ctx.send(embed=gifs.hug(ctx, user))

    @comando.command(help="Ri")
    async def laugh(self, ctx):
        await ctx.send(embed=gifs.laugh(ctx))

    @comando.command(help="Gera um pokémon aleatório")
    async def pokemon(self, ctx):
        await ctx.send(embed=pokemon.pokemon(ctx))



async def setup(bot: commands.Bot):
    await bot.add_cog(Gerais(bot))