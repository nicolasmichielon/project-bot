import discord
import requests
def moeda():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    requisição = requests.get(link)
    requisição_dic = requisição.json()
    descricao = requisição_dic['USDBRL']['high']
    descricao=float(descricao)
    mensagem = (f"**$1,00 = R${descricao: .2f}**")
    embed = discord.Embed(title="💵 Dólar hoje", description=mensagem)
    return embed

