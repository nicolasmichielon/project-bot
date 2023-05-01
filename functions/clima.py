import os
from datetime import datetime
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

from datetime import datetime

def proxClima(city):
    lista = []
    var = 0
    link = f"https://api.openweathermap.org/data/2.5/forecast?q={unidecode(' '.join(city))}&lang=pt_br&appid={os.getenv('API_KEY')}"
    requisição = requests.get(link)
    requisição_dic = requisição.json()
    nome = requisição_dic['city']['name']
    datas = []
    for i in range(4, 39, 8):
        # Converte o campo dt_txt para um objeto datetime e extrai o dia do ano
        dia_do_ano = datetime.strptime(requisição_dic['list'][i]['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m')
        if dia_do_ano not in datas:
            datas.append(dia_do_ano)
            clima = requisição_dic['list'][i]['weather'][0]['description'].upper()
            icone = ''
            if 'NUBLADO' in clima:
                icone = ':cloud:'
            elif 'CHUVA' in clima:
                icone = ':cloud_with_rain:'
            elif 'SOL' in clima or 'CLARO' in clima or 'CÉU LIMPO' in clima:
                icone = ':sunny:'
            elif 'NEVE' in clima:
                icone = ':cloud_with_snow:'
            elif 'ALGUMAS NUVENS' in clima:
                icone= ':white_sun_cloud:'
            lista.append(f"{icone} {clima}")
    embed = discord.Embed(title=f"Previsão do tempo para os próximos 5 dias em {nome}", color=0x1db6e0)
    embed.set_thumbnail(url='https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png')
    for i in range(len(lista)):
        embed.add_field(name=f'{datas[i]}', value=lista[i], inline=False)
    return embed

