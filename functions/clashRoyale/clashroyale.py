import os
import urllib.parse
import pymongo
import requests
from discord import Embed


async def setClanRoyale(clan,guild,ctx):
    """Configura um clan no Clash Royale"""
    try:
        clan = urllib.parse.quote_plus(clan[0])
        link =f"https://api.clashroyale.com/v1/clans/{clan}"
        headers = {
            'Authorization' : f'{os.getenv("API_KEY_CLASHROYALE")}'
        }
        requisicao = requests.get(link,headers)
        requisicao_dic = requisicao.json()
        clannome = requisicao_dic['name']

        mongo = pymongo.MongoClient(os.getenv('DATABASE'))
        db = mongo.serverSettigs


        collection_name = f'{ctx.guild.id}'

        # Verifica se já existe um registro para este servidor
        existing_clan_data = db[collection_name].find_one({'tagclan': {'$exists': True}})
        if existing_clan_data:
            await ctx.send(
                f"Já existe um clã configurado para este servidor.\n"
                f"Deseja sobrescrever os dados? Responda `sim` para confirmar."
            )


            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel


            response = await ctx.bot.wait_for("message", check=check, timeout=60)  # Aguarda a resposta do usuário por 60 segundos

            if response.content.lower() == "sim":
                # Sobrescreve os dados do clã existente
                db[collection_name].update_one(
                    {},
                    {'$set': {
                        'tagclan': clan,
                        'nomedoclan': clannome,
                    }},
                )
                confirmation_text = "Clã sobrescrito com sucesso!"
            else:
                confirmation_text = "Ação cancelada."

            await ctx.send(confirmation_text)
        else:
            db[collection_name].insert_one({
                'tagclan': clan,
                'nomedoclan': clannome,
            })

            await ctx.send(f"Clan {clannome} configurado!")

        # Cria e retorna um objeto Embed
        embed = Embed(description=f"Clan {clannome} configurado")
        return embed
    except Exception as e:
        embed = Embed(description="Erro ao configurar o clã")
        return embed


def searchClanRoyale(clan):
    """Procura um clan no Clash Royale"""
    try:
        clan = urllib.parse.quote_plus(clan[0])
        link =f'https://api.clashroyale.com/v1/clans/{clan}'
        headers = {
            'Authorization' : f'{os.getenv("API_KEY_CLASHROYALE")}'
        }
        requisicao = requests.get(link,headers)
        requisicao_dic = requisicao.json()
        clanName = requisicao_dic['name']
        clantag = requisicao_dic['tag']
        descriptionClan = requisicao_dic['description']
        clanTrophies = requisicao_dic['clanScore']
        clanWarTrophies = requisicao_dic['clanWarTrophies']
        country = requisicao_dic['location']['countryCode']
        clanChest = requisicao_dic['clanChestLevel']
        members = requisicao_dic['members']
        bau = "<:bau:1139171065642369025>"

        embed = Embed(
            title=f"{clanName} :flag_{country.lower()}: {clantag}",
            description=f"**Membros:** {members} | **Troféus do Clã:** {clanTrophies} 🏆\n{bau} **Nível do Baú do Clã:** {clanChest}\n🏆 **Troféus de Guerra do Clã:** {clanWarTrophies}\n**Descrição:** {descriptionClan}",
            color=0x3498db
        )
        return embed
    except:
        embed = Embed(description= "Clan não encontrado")
        return embed

