import random
import requests
from discord import Embed

from functions import gifs


def pokemon(ctx):
    link = "https://pokeapi.co/api/v2/pokedex/1"
    requisição = requests.get(link)
    requisição_dic = requisição.json()
    aleatorio= random.randint(0,1009)
    descricao = requisição_dic['pokemon_entries'][aleatorio]['pokemon_species']['name']
    print(descricao)
    linkPokemon=f"https://pokeapi.co/api/v2/pokemon/{descricao}"
    requisiçãoPoke = requests.get(linkPokemon)
    requisição_dicPoke = requisiçãoPoke.json()
    descricaoPoke = requisição_dicPoke['sprites']['other']['official-artwork']['front_default']
    descricao = descricao.capitalize()
    embed = Embed(title=f"{descricao}")
    embed.set_image(url=descricaoPoke)
    return embed
