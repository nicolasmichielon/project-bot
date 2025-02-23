import json
import os
from os import getenv
from random import randint
import requests
from discord import Embed


def gameSearch(game):
    print(game)
    link= f"https://api.rawg.io/api/games?key={os.getenv('API_KEY_GAME')}&search={game}"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    titulo = requisicao_dic['results'][0]['name']

    print(titulo)
    imagem= requisicao_dic['results'][0]['background_image']
    embed = Embed(title= titulo, description=f"Esse é o jogo")
    embed.set_image(url=imagem)
    return embed

def gameAchievements(game):
    link= f"https://api.rawg.io/api/games?key={os.getenv('API_KEY_GAME')}&search={game}"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    id = requisicao_dic['results'][0]['id']
    link = f"https://api.rawg.io/api/games/{id}/achievements?key={os.getenv('API_KEY_GAME')}&search={game}"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    nome = requisicao_dic['results'][0]['name']
    print(nome)
    descricao = requisicao_dic['results'][0]['description']
    imagem = requisicao_dic['results'][0]['image']
    print(imagem)
    embed = Embed(title= nome, description=f"{descricao}")
    embed.set_image(url=imagem)
    print(embed)
    return embed
