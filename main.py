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
client = commands.Bot(command_prefix="?", intents=intents)


async def load_extensions():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py') and not filename.startswith('__'):
            await client.load_extension(f"cogs.{filename[:-3]}")


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
