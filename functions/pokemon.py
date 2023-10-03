import random
import requests
from discord import Embed

def pokemon(ctx):
    link = "https://pokeapi.co/api/v2/pokedex/1"
    request = requests.get(link)
    request_dic = request.json()
    randons= random.randint(0,1009)
    descriptions = request_dic['pokemon_entries'][randons]['pokemon_species']['name']
    linkPokemon=f"https://pokeapi.co/api/v2/pokemon/{descriptions}"
    requestPoke = requests.get(linkPokemon)
    request_dicPoke = requestPoke.json()
    descriptionPoke = request_dicPoke['sprites']['other']['official-artwork']['front_default']
    types = [tipo['type']['name'] for tipo in request_dicPoke['types']]
    weaknesses = []
    for tipo in request_dicPoke['types']:
        linkType = tipo['type']['url']
        requestType = requests.get(linkType)
        request_dicType = requestType.json()
        weaknesses += [weakness['name'] for weakness in request_dicType['damage_relations']['double_damage_from']]
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
    titulo = f"{descriptions.capitalize()}\nTipo: {' '.join(emojis[type] for type in types)}\nFraquezas: {' '.join(emojis[fraqueza] for fraqueza in weaknesses)}"
    embed = Embed(title=titulo)
    embed.set_image(url=descriptionPoke)
    return embed
