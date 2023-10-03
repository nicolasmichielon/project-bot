import requests
import discord
import os

from unidecode import unidecode


def convert_to_stars(rating):
    """Converte a classificação do filme em estrelas"""
    if rating % 1 == 0.5:
        rounded_rating = round(rating)
        if rounded_rating % 2 != 0:
            rounded_rating += 1
    else:
        rounded_rating = round(rating)

    # Define the star emojis representing each rating level
    estrelainteira = "<:estrelainteira:1133432382318444626>"
    meiaestrela = "<:meiaestrela:1133432379667660840>"

    estrelas, resto = divmod(int(rounded_rating), 2)
    meia_estrela = bool(resto)

    estrelas_str = estrelainteira * estrelas

    if meia_estrela:
        estrelas_str += meiaestrela

    return estrelas_str or 'N/A'

def searchMovie(movie):
    """Procura um filme"""

    link = f"https://api.themoviedb.org/3/search/movie?language=pt-BR&query={unidecode('+'.join(movie))}&api_key={os.getenv('API_KEY_FILME')}"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    titulo = requisicao_dic['results'][0]['title']
    descricao = requisicao_dic['results'][0]['overview']
    imagemReq = requisicao_dic['results'][0]['poster_path']
    imagem = f"https://image.tmdb.org/t/p/w500/{imagemReq}"
    avaliacao = float(requisicao_dic['results'][0]['vote_average'])
    estrelas = convert_to_stars(avaliacao)
    avaliacao = avaliacao/2
    embed_color = int('9370DB', 16)
    embed = discord.Embed(title=f"{titulo}", description=f"{descricao}", color=embed_color)
    embed.set_image(url=imagem)
    embed.add_field(name='Avaliação', value=estrelas + f" **{round(avaliacao, 1)}/5**", inline=False)

    return embed
