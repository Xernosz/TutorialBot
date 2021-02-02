# Importing Shit
import discord
from discord.ext import commands, tasks
# Importing Shit

# Setup
client = commands.Bot(command_prefix='%')
# Setup

# Events
## Making sure the bot is online
@client.event
async def on_ready():
	print("Bot is ready!")
## Making sure the bot is online

# Events

# Commands

## Ping
@client.command()
async def ping(ctx):
	await ctx.send('Pong!')
## Ping
# Commands

client.run('YOUR_TOKEN')
