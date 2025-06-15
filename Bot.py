import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

TOKEN = 'MTM4MzQ1MDk1NjU0ODY2OTUyMQ.GwY-C9.dXZKu31KCtsgkHbflblfSsHi7qPW35f3S6D9bg'

@bot.event
async def on_ready():
    print("Bot online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(774662531917676585)
    text = f"Welcome to the server, {member.mention}!"
    emmbed = discord.Embed(title = 'Welcome to server!',
                           description = text,
                           color = 0x66FFFF)
    await channel.send(text)
    await channel.send(embed = emmbed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1383457719620468796)
    text = f"{member.mention} has left the server!"
    emmbed = discord.Embed(title='Left to server!',
                           description=text,
                           color=0x66FFFF)
    await channel.send(text)
    await channel.send(embed = emmbed)

bot.run(TOKEN)
