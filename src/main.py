from decouple import config
import random
import discord # https://pypi.org/project/discord.py/
from discord.ext import commands

DISCORD_TOKEN = config('DISCORD_TOKEN')
DATAFILE_PATH = config('DATAFILE_PATH')

# TODO save list in a file
LISTS = {}

bot = commands.Bot(command_prefix='>')

@bot.command(name='ping')
async def _ping(ctx):
    await ctx.send('pong')

# command add :list :item
@bot.command(name='add')
async def _add(ctx, key, item):
    if key not in LISTS:
        LISTS[key] = []
    if item not in LISTS[key]:
        LISTS[key].append(item)
    await ctx.send('saved')

# command remove :list :item
@bot.command(name='remove')
async def _remove(ctx, key, item):
    try:
        LISTS[key].remove(item)
        await ctx.send('saved')
    except:
        await ctx.send('{} not found'.format(item))

# command pick :list
@bot.command(name='pick')
async def _pick(ctx, key):
    try:
        await ctx.send(random.choice(LISTS[key]))
    except:
        await ctx.send('List not found')

# command list :list
@bot.command(name='list')
async def _list(ctx, key):
    try:
        await ctx.send('\n'.join(LISTS[key]))
    except:
        await ctx.send('List not found')

bot.run(DISCORD_TOKEN)
