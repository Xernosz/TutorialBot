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
    await client.change_presence(
        activity=discord.Game(
            name=f"NIEN: {len(client.guilds)} servers!"))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    print(f'{round(client.latency * 1000)}ms')
    print(f'In: {len(client.guilds)} servers!')
## When Ready
# Events

# Commands
## Ping-
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! The latency is: {round(client.latency * 1000)} miliseconds!")
## Ping
# Commands
client.run('YOUR_TOKEN