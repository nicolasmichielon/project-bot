import discord
from newsapi import NewsApiClient
import os

newsapi = NewsApiClient(api_key=os.getenv('API_NEWS'))


def searchNews(termo):
    termo = " ".join(termo)
    print(termo)
    pesquisa = newsapi.get_everything(language='pt',
                                     q=termo,
                                     sort_by='relevancy',
                                     page=1)
    print(pesquisa.get('articles')[0])
    title = pesquisa.get('articles')[0].get('title')
    description = pesquisa.get('articles')[0].get('description')
    author = pesquisa.get('articles')[0].get('author')
    url = pesquisa.get('articles')[0].get('url')
    urlToImage = pesquisa.get('articles')[0].get('urlToImage')
    print(urlToImage)

    print(title)
    print(description)
    embed = discord.Embed(title=":newspaper:  "+title, description=f"```{description}```", url=url)
    embed.set_image(url=urlToImage)

    return embed
