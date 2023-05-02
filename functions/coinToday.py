import discord
import requests
def realToday():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,ARS-BRL"
    request = requests.get(link)
    request_dic = request.json()
    descriptionsDollar=float(request_dic['USDBRL']['high'])
    descriptionsArg=float(request_dic['ARSBRL']['high'])
    descriptionsEuro= float(request_dic['EURBRL']['high'])
    message = (f"**:flag_us: $1,00 = R${descriptionsDollar: .2f}\n:flag_ar: $1,00 = R${descriptionsArg: .2f}\n:flag_eu: €1,00 = R${descriptionsEuro: .2f}**")
    embed = discord.Embed(title="💵 Real hoje", description=message)
    return embed
def dollarToday():
    link = "https://economia.awesomeapi.com.br/last/CHF-USD,EUR-USD,GBP-USD"
    request = requests.get(link)
    request_dic = request.json()
    descriptionsReal=float(request_dic['CHFUSD']['high'])
    descriptionsGdp=float(request_dic['GBPUSD']['high'])
    descriptionsEuro= float(request_dic['EURUSD']['high'])
    message = (f"**:flag_ch: Fr.1,00 = ${descriptionsReal: .2f}\n:flag_gb: £1,00 = ${descriptionsGdp: .2f}\n:flag_eu: €1,00 = ${descriptionsEuro: .2f}**")
    embed = discord.Embed(title="💵 Dólar hoje", description=message)
    return embed

