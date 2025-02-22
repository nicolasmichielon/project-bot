import asyncio

import discord
import pymongo
from dotenv import load_dotenv
from translate import Translator
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
translator = Translator(to_lang="pt-br")
client = commands.Bot(command_prefix="?", intents=intents,help_command=None)


async def load_extensions():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py') and not filename.startswith('__'):
            await client.load_extension(f"cogs.{filename[:-3]}")


@client.listen()
async def on_message(message):
    if message.content == "?help":
        command_list = {
            "Utilities Functions": [
                ("?clear", "Apaga x mensagens"),
                ("?weather", "Ver o clima agora"),
                ("?forecast", "Ver o clima nos próximos 5 dias"),
                ("?roll", "Rola um dado até X valor limite"),
                ("?coinflip", "Cara ou coroa"),
                ("?dollar", "Ver o valor do dólar hoje"),
                ("?real", "Ver o valor do real hoje"),
            ],
            "Fun Functions": [
                ("?gif", "Procure um gif"),
                ("?searchmovie", "Pesquisa um filme"),
                ("?hug", "Dê um abraço no seu amigo"),
                ("?joke", "Conta uma piada"),
                ("?kiss", "Dê um beijo no seu amigo"),
                ("?laugh", "Ri"),
                ("?news", "Pesquisar uma notícia"),
                ("?pokemon", "Gerar um Pokémon aleatório"),
                ("?punch", "Dê um soco no seu amigo"),
                ("?slap", "Dê um tapa no seu amigo"),
                ("?searchClanCR", "Pesquisa um clan no Clash Royale")
            ]
        }

        pages = []

        presentation_embed = discord.Embed(
            title=f"Olá, sou o {client.user.name}! ",
            description="Sou um bot em fase de teste, tentando me adaptar à esse mundo.",
            color=discord.Color.blue()
        )
        presentation_embed.set_footer(text="Page 1/3")
        pages.append(presentation_embed)

        for category, commands in command_list.items():
            embed = discord.Embed(
                title=f"{category}",
                color=discord.Color.green()
            )
            for name, value in commands:
                embed.add_field(name=name, value=value, inline=False)
            embed.set_footer(text=f"Page {len(pages)+1}/{len(command_list)+1}")

            pages.append(embed)

        current_page = 0
        help_msg = await message.channel.send(embed=pages[current_page])
        await help_msg.add_reaction("◀️")  # Previous page
        await help_msg.add_reaction("▶️")  # Next page

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            except TimeoutError:
                break
#and current_page > 0
            if str(reaction.emoji) == "◀️":
                if current_page > 0:
                    current_page -= 1
                else:
                    current_page = 2
#and current_page < len(pages) - 1
            elif str(reaction.emoji) == "▶️":
                if current_page < len(pages) -1:
                    current_page += 1
                else:
                    current_page = 0
            await help_msg.edit(embed=pages[current_page])

@client.listen()
async def on_message(message):
    if message.author == client.user:
        return

# Conecta ao banco de dados MongoDB
mongo = pymongo.MongoClient(os.getenv('DATABASE'))
db = mongo.serveruser
@client.event
async def on_guild_join(guild):
    print(f'Bot entrou no servidor: {guild.name} (ID: {guild.id})')
    print(guild.members)
    # Crie a coleção se ela não existir
    collection_name = f'{guild.id}'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    # Agora você pode trabalhar com a lista completa de membros
    # Crie uma lista de usuários do servidor
    users = []
    for member in guild.members:
        if member.discriminator == '0':
            users.append({
                'user_id': member.id,
                'username': member.name,
                'server_id': guild.id
            })

    try:
        # Insira a lista de usuários no banco de dados
        for user in users:
            db[collection_name].update_one(
                {'user_id': user['user_id']},
                {'$set': {
                    'username': user['username'],
                }},
                upsert=True
            )

        saved_users = db[collection_name].find({'server_id': guild.id})
        for user in saved_users:
            print(f'Usuário salvo: {user["username"]}')
    except Exception as e:
        print(f'Erro ao inserir dados: {e}')



@client.listen()
async def on_ready():
    print('Bot online')
load_dotenv()

async def main():
    async with client:
        await load_extensions()
        await client.start(os.getenv('DISCORD_TOKEN'))


asyncio.run(main())
