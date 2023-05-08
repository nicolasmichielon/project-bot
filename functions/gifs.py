import json
from os import getenv
from random import randint
import requests
from discord import Embed

# set the apikey and limit
apikey = getenv("API_KEY_TENOR")
lmt = 20
ckey = "my_test_app"  # set the client_key for the integration and use the same value for all API calls


def gif_search(search_term):
    if type(search_term) is list:
        search_term = ' '.join(search_term)

    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        gif = json.loads(r.content)
        url = gif.get('results')[randint(0, lmt)].get('media_formats').get('gif').get('url')
        return url
    else:
        return "Nenhum GIF encontrado."


def slap(ctx, user):
    gif_url = gif_search('anime slap')
    embed = Embed(description=f"{ctx.author.mention} deu um tapa em {user}")
    embed.set_image(url=gif_url)
    return embed


def kiss(ctx, user):
    gif_url = gif_search('anime kiss')
    embed = Embed(description=f"{ctx.author.mention} beijou {user}")
    embed.set_image(url=gif_url)
    return embed


def punch(ctx, user):
    gif_url = gif_search('anime punch')
    embed = Embed(description=f"{ctx.author.mention} socou {user}")
    embed.set_image(url=gif_url)
    return embed


def hug(ctx, user):
    gif_url = gif_search('anime hug')
    embed = Embed(description=f"{ctx.author.mention} abraçou {user}")
    embed.set_image(url=gif_url)
    return embed


def laugh(ctx):
    gif_url = gif_search('anime laugh')
    embed = Embed(description=f"{ctx.author.mention} ri, apenas.")
    embed.set_image(url=gif_url)
    return embed