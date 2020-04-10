# TODO import from env

import random
# https://pypi.org/project/discord.py/
import discord
from discord.ext import commands

DISCORD_TOKEN = config('DISCORD_TOKEN')
LISTS = {}
bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# command add :list :item
@bot.command()
async def add(ctx, key, item):
    if key not in LISTS:
        LISTS[key] = []
    if item not in LISTS[key]:
        LISTS[key].append(item)
    await ctx.send('saved')

# command remove :list :item
@bot.command()
async def remove(ctx, key, item):
    try:
        LISTS[key].remove(item)
        await ctx.send('saved')
    except:
        await ctx.send('{} not found'.format(item))

# TODO command pick :list
@bot.command()
async def pick(ctx, key):
    try:
        await ctx.send(random.choice(LISTS[key]))
    except:
        await ctx.send('List not found')

# TODO command list :list
@bot.command()
async def list(ctx, key):
    try:
        await ctx.send(random.choice(LISTS[key]))
    except:
        await ctx.send('List not found')

bot.run(DISCORD_TOKEN)
