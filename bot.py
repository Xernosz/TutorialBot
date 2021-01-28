# Importing Stuff
import discord
from discord.ext import commands, tasks
# Importing Stuff

# Setup
client=commands.Bot(command_prefix='|')
# Setup

# Events
## When Ready
@client.event
async def on_ready():
    print('bot is ready!')
## When Ready
# Events

# Commands
## Ping-
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")
## Ping
# Commands
client.run('ODA0NDYyODU0NTMwNjYyNDEx.YBMsag.TuWcDfYho4clKR7jYANHHk8KHlU')
