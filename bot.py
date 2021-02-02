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
	strem = discord.Game(name="Do %help")
	await client.change_presence(status=discord.Status.dnd, activity=strem)
	print(f"Connected to Bot: {client.user.name}")
	print(f"Bot ID: {client.user.id}")
	print(f"Currently in: {len(client.guilds)} server(s)!")
	print(f"The current latency of the bot is {round(client.latency * 1000)} ms")
## Making sure the bot is online

# Events

# Commands

## Ping
@client.command(aliases=["latency"])
async def ping(ctx):
	await ctx.send(f"Pong! The latency is: {round(client.latency * 1000)} miliseconds!")
## Ping
# Commands

client.run('YOUR_TOKEN')
