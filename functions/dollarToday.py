import discord
import requests
def coin():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    request = requests.get(link)
    request_dic = request.json()
    descriptions = request_dic['USDBRL']['high']
    descriptions=float(descriptions)
    message = (f"**$1,00 = R${descriptions: .2f}**")
    embed = discord.Embed(title="💵 Dólar hoje", description=message)
    return embed

