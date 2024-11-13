import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
discord_token = os.getenv("KEY")


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mute(ctx):
    # Check if the command is invoked in a voice channel
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("You need to be in a voice channel to use this command!")
        return

    # Mute all members in the voice channel
    for member in ctx.author.voice.channel.members:
        await member.edit(mute=True)
    await ctx.send("Members have been muted!")

@bot.command()
async def unmute(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
      await ctx.send("You need to be in a voice channel to use this command!")
      return

    for member in ctx.author.voice.channel.members:
      await member.edit(mute=False)

bot.run(discord_token)
