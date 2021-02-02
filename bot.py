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
	print(f"Connected to Bot: {client.user.name}")
	print(f"Bot ID: {client.user.id}")
	print(f"Currently in: {len(client.guilds)} server(s)!")
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
