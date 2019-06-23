import discord
import aiohttp
from discord.ext import commands

bot = commands.Bot(command_prefix='#')
token = 'NTc5Njc0MDE2Mzk5MjI4OTI4.XQ9wjQ.8srSWEMN4JPQhOvba1E6CdXPSeg'

@bot.event
async def on_ready():
    print('alisa connected from server')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="за порядком"))

@bot.command('alisa')
async def on_message(message):
    await message.channel.send('?')

@bot.command('join')
async def join_voice(message):
     channel = message.message.author.voice.channel
     await channel.connect()

@bot.command('leave')
async def leave(message):
    channel = message.message.guild.voice_client
    await channel.disconnect()

@bot.command('cats')
async def get_session(message):
    channel = message.message.channel
    async with aiohttp.ClientSession() as session:
        channel = message.message.channel
        async with session.get('http://aws.random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()
                await channel.send(js['file'])
bot.run(token)
