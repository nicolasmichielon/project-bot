import asyncio
import requests
import discord
from discord.ext import commands

async def searchNews(ctx):
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    top_stories = response.json()

    current_page = 0
    stories_per_page = 5
    stories_per_request = 50
    pages = len(top_stories) // stories_per_page

    def get_embed():
        embed = discord.Embed(title="Top Stories on Hacker News", color=0xff5733)

        start = current_page * stories_per_page
        end = start + stories_per_page
        for i, story_id in enumerate(top_stories[start:end], start=start):
            story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
            story = story_response.json()
            story_title = story.get("title")
            story_url = story.get("url")
            story_score = story.get("score")
            story_descendants = story.get("descendants")

            embed.add_field(name=f"**{i + 1}. {story_title}**", value=f"{story_score} points, {story_descendants} comments, [read]({story_url})", inline=False)

        embed.set_footer(text=f"Page {current_page + 1} of {pages + 1}")
        return embed

    message = await ctx.send(embed=get_embed())
    if pages == 0:
        return

    # Add reactions to change the page
    reactions = ['⏮', '◀', '▶', '⏭']
    for reaction in reactions:
        await message.add_reaction(reaction)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reactions

    while True:
        try:
            reaction, user = await ctx.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return

        if str(reaction.emoji) == '◀' and current_page > 0:
            current_page -= 1
            await message.edit(embed=get_embed())
        elif str(reaction.emoji) == '▶' and current_page < pages:
            current_page += 1
            if current_page * stories_per_page % stories_per_request == 0:
                # Request next batch of stories
                start_index = current_page * stories_per_page
                end_index = start_index + stories_per_request
                top_stories = response.json()[start_index:end_index]
            await message.edit(embed=get_embed())
        elif str(reaction.emoji) == '⏮':
            current_page = 0
            await message.edit(embed=get_embed())
        elif str(reaction.emoji) == '⏭':
            current_page = pages
            await message.edit(embed=get_embed())

        await reaction.remove(user)  # Remove user's reaction to keep the message clean
