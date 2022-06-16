import os
import random
import discord
intents = discord.Intents.default()
from discord.ext import commands
from dotenv import load_dotenv

intents.members = True
intents.typing = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='.', intents=intents)
client = discord.Client()

@bot.event
async def on_ready():
    print('bot is up and running')


""" Commands """

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command(brief='Says ping and shows you latency', description='Responds with ping and shows you latency')
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong mother fu- your latency is {round(bot.latency * 1000)} ms')


@bot.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5): # Set default value to None
    if amount == None:
        await ctx.channel.purge(limit=100)
    else:
        try:
            int(amount)
        except: # Error handler
            await ctx.send('Please enter a valid integer as amount.')
        else:
            await ctx.channel.purge(limit=amount)

@bot.command(aliases=['member', 'mem', 'mems', 'meb'])
async def members(ctx):
    for guild in bot.guilds:
        for member in guild.members:
            await ctx.send(member)



bot.run(TOKEN)