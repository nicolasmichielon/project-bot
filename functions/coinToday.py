import discord
import requests


def realToday():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,ARS-BRL"
    request = requests.get(link)
    request_dic = request.json()
    descriptions_dollar = float(request_dic['USDBRL']['high'])
    descriptions_arg = float(request_dic['ARSBRL']['high'])
    descriptions_euro = float(request_dic['EURBRL']['high'])
    message = f"**:flag_us: $1,00 = R${descriptions_dollar: .2f}\n:flag_ar: $1,00 = R${descriptions_arg: .2f}\n" \
              f":flag_eu: €1,00 = R${descriptions_euro: .2f}** "
    embed = discord.Embed(title="💵 Real hoje", description=message)
    return embed


def dollarToday():
    link = "https://economia.awesomeapi.com.br/last/CHF-USD,EUR-USD,GBP-USD"
    request = requests.get(link)
    request_dic = request.json()
    descriptions_real=float(request_dic['CHFUSD']['high'])
    descriptions_gdp=float(request_dic['GBPUSD']['high'])
    descriptions_euro= float(request_dic['EURUSD']['high'])
    message = f"**:flag_ch: Fr.1,00 = ${descriptions_real: .2f}\n:flag_gb: £1,00 = ${descriptions_gdp: .2f}\n:flag_eu" \
              f": €1,00 = ${descriptions_euro: .2f}** "
    embed = discord.Embed(title="💵 Dólar hoje", description=message)
    return embed

