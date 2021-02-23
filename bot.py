# Importing Shit
import discord
from discord.ext import commands, tasks
import random
# Importing Shit

# Setup
client = commands.Bot(command_prefix='%')
# Setup
client.remove_command("help")
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
                 'Very doubtful.']
    if question:
        await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')
    else:
        await ctx.send("You must ask a question for the magic 8-ball to answer!")

## 8Ball

## Help
@client.command()
async def help(ctx):
 embed = discord.Embed(title="Commands for this bot!", description="If you need more help contact the owner of this bot.", colour=0xFF000)
 embed.set_author(name="Bot")
 embed.set_image(url="https://cdn.discordapp.com/avatars/806097137237884958/a029f2f2ee1fd85707cd072164b782f0.png?size=128")
 embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/806097137237884958/a029f2f2ee1fd85707cd072164b782f0.png?size=128")
 embed.add_field(name="Ping", value="Tests if the bot is working and what the latency is!", inline=True)
 embed.add_field(name="8Ball", value="Randomizes a question with a answer and gives it to you!")
 embed.set_footer(text="Make sure to read the rules first.")
 await ctx.send(embed=embed)



## Help

## Hug
@client.command()
async def hug(ctx, user: discord.User, *, Notes):
	hugGifs = ["https://media.giphy.com/media/143v0Z4767T15e/giphy.gif",
	"https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
	"https://media.giphy.com/media/kvKFM3UWg2P04/giphy.gif",
	"https://media.giphy.com/media/wnsgren9NtITS/giphy.gif",
	"https://media.giphy.com/media/HaC1WdpkL3W00/giphy.gif",
	"https://media.giphy.com/media/yziFo5qYAOgY8/giphy.gif",
	"https://media.giphy.com/media/cotftb3AXgfV6/giphy.gif",
	"https://media.giphy.com/media/cotftb3AXgfV6/giphy.gif"
	"https://media2.giphy.com/media/vJ3PqQ1qTsEV2/giphy.gif?cid=ecf05e47fc48741d2ff3569c13417634a10afba74cd8517d&rid=giphy.gif"]
	embed = discord.Embed(title=None, description=f"{ctx.message.author.mention} hugs {user.mention}, {Notes}")
	embed.set_image(url=random.choice(hugGifs))

	await ctx.send(embed=embed)
## Hug

## Kick
@client.command()
async def kick(ctx, user: discord.User, *, reason):
	await user.kick(reason=reason)
	await ctx.send(f'{user.mention} has been kicked by {ctx.message.author.mention} for reason of: {reason}!')
## Kick

## Ban
@client.command()
async def ban(ctx, user: discord.User, *, reason):
	await user.ban(reason=reason)
	await ctx.send(f'{user.mention} has been banned by {ctx.message.author.mention} for reason of: {reason}!')
## Ban

# Commands

client.run('ODA2MDk3MTM3MjM3ODg0OTU4.YBkedg.EpRdgithJItdVvJoTn_913cML_4')
