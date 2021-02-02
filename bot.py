import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='%')

@client.event
async def on_ready():
	print("Bot is ready!")


@client.command()
async def ping(ctx):
	await ctx.send('Pong!')

client.run('ODA2MDk3MTM3MjM3ODg0OTU4.YBkedg.z2TIFvq101YXGOhVewnVn1Lec9Y')
