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
    tipos = [tipo['type']['name'] for tipo in requisição_dicPoke['types']]
    fraquezas = []
    for tipo in requisição_dicPoke['types']:
        linkTipo = tipo['type']['url']
        requisiçãoTipo = requests.get(linkTipo)
        requisição_dicTipo = requisiçãoTipo.json()
        fraquezas += [fraqueza['name'] for fraqueza in requisição_dicTipo['damage_relations']['double_damage_from']]
    emojis = {
        'normal': ':white_large_square:',
        'fire': ':fire:',
        'water': ':droplet:',
        'electric': ':zap:',
        'grass': ':leaves:',
        'ice': ':snowflake:',
        'fighting': ':boxing_glove:',
        'poison': ':skull:',
        'ground': ':mountain:',
        'flying': ':eagle:',
        'psychic': ':crystal_ball:',
        'bug': ':bug:',
        'rock': ':mountain:',
        'ghost': ':ghost:',
        'dragon': ':dragon:',
        'dark': ':black_square_button:',
        'steel': ':gear:',
        'fairy': ':sparkles:'
    }
    titulo = f"{descricao.capitalize()}\nTipo: {' '.join(emojis[tipo] for tipo in tipos)}\nFraquezas: {' '.join(emojis[fraqueza] for fraqueza in fraquezas)}"
    embed = Embed(title=titulo)
    embed.set_image(url=descricaoPoke)
    return embed
