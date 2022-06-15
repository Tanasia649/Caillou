import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='c.')

@client.event
async def on_ready():
    print('{0.user} is now logged in'.format(client))


client.run(TOKEN)