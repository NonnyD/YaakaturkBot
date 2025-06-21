import asyncio
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

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

@bot.command()
async def poke(ctx, member: discord.Member):
    if member.voice and member.voice.channel:
        original_channel = member.voice.channel
        temp_channel = None
        guild = ctx.guild
        temp_channel = await guild.create_voice_channel(name="poke-temp", reason="Poke someone")

        try:

            await member.send(f"คุณถูก {ctx.author.display_name} poke! 😄")

            await member.move_to(temp_channel)
            await member.move_to(original_channel)

            await member.move_to(temp_channel)
            await member.move_to(original_channel)

            await member.move_to(temp_channel)
            await member.move_to(original_channel)

        except Exception as e:
            await ctx.send(f'Error: {e}')
        finally:
            await asyncio.sleep(1)
            await temp_channel.delete()
    else:
        await ctx.send(f"{member.display_name} is not in a voice channel!")
        

bot.run(os.getenv("BOT_TOKEN"))
