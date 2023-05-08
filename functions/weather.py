from os import getenv
from datetime import datetime
import discord
from unidecode import unidecode
import requests
from datetime import datetime


def weather(city):
    print(' '.join(city))
    link =f"https://api.openweathermap.org/data/2.5/weather?q={unidecode(' '.join(city))}&lang=pt_br&appid={getenv('API_KEY')}"

    requisição = requests.get(link)
    requisição_dic=requisição.json()
    descricao = requisição_dic['weather'][0]['description']
    temp = requisição_dic['main']['temp'] -273.15

    return str(f"A temperatura está em {temp: .2f}") + " ºC, " + descricao


def forecast(city):
    list = []
    link = f"https://api.openweathermap.org/data/2.5/forecast?q={unidecode(' '.join(city))}&lang=pt_br&appid={getenv('API_KEY')}"
    request = requests.get(link)
    request_dic = request.json()
    name = request_dic['city']['name']
    dates = []
    for i in range(4, 39, 8):
        dayOfTheYear = datetime.strptime(request_dic['list'][i]['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m')
        if dayOfTheYear not in dates:
            dates.append(dayOfTheYear)
            weather = request_dic['list'][i]['weather'][0]['description'].upper()
            icon = ''
            if 'NUBLADO' in weather:
                icon = ':cloud:'
            elif 'CHUVA' in weather:
                icon = ':cloud_with_rain:'
            elif 'SOL' in weather or 'CLARO' in weather or 'CÉU LIMPO' in weather:
                icon = ':sunny:'
            elif 'NEVE' in weather:
                icon = ':cloud_with_snow:'
            elif 'ALGUMAS NUVENS' in weather:
                icon= ':white_sun_cloud:'
            list.append(f"{icon} {weather}")
    embed = discord.Embed(title=f"Previsão do tempo para os próximos 5 dias em {name}", color=0x1db6e0)
    embed.set_thumbnail(url='https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png')
    for i in range(len(list)):
        embed.add_field(name=f'{dates[i]}', value=list[i], inline=False)
    return embed

