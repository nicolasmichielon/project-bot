import random
import requests
from discord import Embed

def pokemon(ctx):
    """Procurar o pokemon e imprimi-lo, mostrando o tipo, suas vantagens e desvantagens"""
    link = "https://pokeapi.co/api/v2/pokedex/1"
    request = requests.get(link)
    request_dic = request.json()
    randons= random.randint(0,1009)
    descriptions = request_dic['pokemon_entries'][randons]['pokemon_species']['name']
    link_pokemon=f"https://pokeapi.co/api/v2/pokemon/{descriptions}"
    request_poke = requests.get(link_pokemon)
    request_dic_poke = request_poke.json()
    description_poke = request_dic_poke['sprites']['other']['official-artwork']['front_default']
    types = [tipo['type']['name'] for tipo in request_dic_poke['types']]
    weaknesses = []
    for tipo in request_dic_poke['types']:
        link_type = tipo['type']['url']
        request_type = requests.get(link_type)
        request_dic_type = request_type.json()
        weaknesses += [weakness['name'] for weakness in request_dic_type['damage_relations']['double_damage_from']]
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
    embed.set_image(url=description_poke)
    return embed
