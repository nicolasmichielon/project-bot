import os

import requests
cidade = "Florianópolis"
def climaAgora():
    link =f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang=pt_br&appid={os.getenv('API_KEY')}"

    requisição = requests.get(link)
    requisição_dic=requisição.json()
    descricao = requisição_dic['weather'][0]['description']
    temp = requisição_dic['main']['temp'] -273.15

    return str(f"A temperatura está em {temp: .2f}") + " ºC, " + descricao

def proxClima():
    link = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&lang=pt_br&appid={os.getenv('API_KEY')}"
    requisição = requests.get(link)
    requisição_dic=requisição.json()
    print(requisição_dic)
    descricao = requisição_dic['weather'][0]['description']
    temp = requisição_dic['main']['temp'] -273.15
    return str(f"A temperatura está em {temp: .2f}") + " ºC, " + descricao
