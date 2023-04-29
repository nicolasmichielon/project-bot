import os

import discord
from unidecode import unidecode
import requests


def climaAgora(city):
    print(' '.join(city))
    link =f"https://api.openweathermap.org/data/2.5/weather?q={unidecode(' '.join(city))}&lang=pt_br&appid={os.getenv('API_KEY')}"

    requisição = requests.get(link)
    requisição_dic=requisição.json()
    descricao = requisição_dic['weather'][0]['description']
    temp = requisição_dic['main']['temp'] -273.15

    return str(f"A temperatura está em {temp: .2f}") + " ºC, " + descricao

def proxClima(city):
    lista=[]
    var=0
    link = f"https://api.openweathermap.org/data/2.5/forecast?q={unidecode(' '.join(city))}&lang=pt_br&appid={'13e6fa6dfc3186b91c69776d6a59a910'}"
    requisição = requests.get(link)
    requisição_dic=requisição.json()
    nome = requisição_dic['city']['name']
    for i in range(4,39,8):
        requisição_dic1 = requisição_dic['list'][i]['weather'][0]['description']
        lista.append(requisição_dic1)
    embed = discord.Embed(title=f"Clima daqui a 5 dias em {nome}  ", description=f"dia 1 -> {lista[0]} \ndia 2 -> {lista[1]} \ndia 3 -> {lista[2]} \ndia 4 -> {lista[3]} \ndia 5 -> {lista[4]}")
    return embed


