# Importing Shit
import discord
from discord.ext import commands, tasks
import random
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
	print(f"Latency = {round(client.latency * 1000)} ms")
## Making sure the bot is online

# Events

# Commands

## Ping
@client.command(aliases=["latency"])
async def ping(ctx):
	await ctx.send(f"The current latency is: {round(client.latency * 1000)} miliseconds")
## Ping

## 8Ball
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [' It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don\'t count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.', ]
    if question:
        await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')
    else:
        await ctx.send("You must ask a question for the magic 8-ball to answer!")

## 8Ball
# Commands

client.run('YOUR_TOKEN')
