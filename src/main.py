# TODO import from env

# https://pypi.org/project/discord.py/
import discord
from discord.ext import commands

DISCORD_TOKEN = config('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# TODO command add :cat :item
# TODO command remove :cat :item
# TODO command pick :cat
# TODO command list :cat

bot.run(DISCORD_TOKEN)
