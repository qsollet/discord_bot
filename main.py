from decouple import config
import random
import discord # https://pypi.org/project/discord.py/
from discord.ext import commands

DISCORD_TOKEN = config('DISCORD_TOKEN')
DATAFILE_PATH = config('DATAFILE_PATH')
COMMAND_PREFIX = config('COMMAND_PREFIX', default='!')
REACTION_EMOJI = config('REACTION_EMOJI', default='✅')

# TODO save list in a file, pickle?
LISTS = {}

bot = commands.Bot(command_prefix=COMMAND_PREFIX)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now connected to Discord')

@bot.command(name='ping', help='Do the pong')
async def _ping(ctx):
    await ctx.message.add_reaction('🏓')

# command add :list :item
@bot.command(name='add', help='Add one or many item to a list')
async def _add(ctx, list_name, *items):
    if list_name not in LISTS:
        LISTS[list_name] = []
    for item in items:
        if item not in LISTS[list_name]:
            LISTS[list_name].append(item)
    await ctx.message.add_reaction(REACTION_EMOJI)

# command remove :list :item
@bot.command(name='remove', help='Remove one or many item from a list')
async def _remove(ctx, list_name, *items):
    try:
        for item in items:
            LISTS[list_name].remove(item)
    except:
        pass
    finally:
        await ctx.message.add_reaction(REACTION_EMOJI)

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
