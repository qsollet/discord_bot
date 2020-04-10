from decouple import config
import random
import discord # https://pypi.org/project/discord.py/
from discord.ext import commands

DISCORD_TOKEN = config('DISCORD_TOKEN')
DATAFILE_PATH = config('DATAFILE_PATH')

# TODO save list in a file, pickle?
LISTS = {}

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now connected to Discord')

@bot.command(name='ping', help='just replies pong')
async def _ping(ctx):
    await ctx.send('pong')

# command add :list :item
@bot.command(name='add', help='Add one or many item to a list')
async def _add(ctx, list_name, *items):
    if list_name not in LISTS:
        LISTS[list_name] = []
    for item in items:
        if item not in LISTS[list_name]:
            LISTS[list_name].append(item)
    await ctx.send('saved `{}` in list `{}`'.format(', '.join(items), list_name))

# command remove :list :item
@bot.command(name='remove', help='Remove one or many item from a list')
async def _remove(ctx, list_name, *items):
    try:
        for item in items:
            LISTS[list_name].remove(item)
        await ctx.send('removed `{}` in list `{}`'.format(', '.join(items), list_name))
    except:
        await ctx.send('`{}` not found'.format(item))

# command pick :list
@bot.command(name='pick', help='Pick an item randomly from a list')
async def _pick(ctx, list_name):
    try:
        await ctx.send(random.choice(LISTS[list_name]))
    except:
        await ctx.send('List `{}` not found'.format(list_name))

# command list :list
@bot.command(name='list', help='Display all items of a list')
async def _list(ctx, list_name):
    try:
        await ctx.send('\n'.join(['{}. {}'.format(i+1, x) for i,x in enumerate(LISTS[list_name])]))
    except:
        await ctx.send('List `{}` not found'.format(list_name))

bot.run(DISCORD_TOKEN)
