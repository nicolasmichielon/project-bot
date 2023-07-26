import asyncio
import discord
from dotenv import load_dotenv
from translate import Translator
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True
translator = Translator(to_lang="pt-br")
client = commands.Bot(command_prefix='?', intents=intents)  # prefix our commands with '.'


async def load_extensions():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py') and not filename.startswith('__'):
            await client.load_extension(f"cogs.{filename[:-3]}")


@client.listen()
async def on_message(message):
    if message.author == client.user:
        return


@client.listen()
async def on_ready():
    print('Bot online')
load_dotenv()


async def main():
    async with client:
        await load_extensions()
        await client.start(os.getenv('DISCORD_TOKEN'))

asyncio.run(main())
