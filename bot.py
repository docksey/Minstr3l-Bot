import discord
import os
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.ext import commands
from data import data
from mapper import mapper

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('TEST_DISCORD_GUILD')
AUTHURL = os.getenv('OAUTH2_URL')
RYTHM = os.getenv('RYTHMBOT_ID')

bot = commands.Bot(command_prefix='$')
db = data()
mapper = mapper()

@bot.event
async def on_ready():
    guilds = db.db_test()

    guild = discord.utils.get(bot.guilds, name=GUILD)
    #bot.loop.create_task(get_queue())

    print(
        f'{bot.user.name} has connected to Discord!\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@bot.event
async def on_message(message):
    if f"{message.author.id}" == RYTHM:
        track = mapper.get_track_from_message(message)
        response = db.upsert_track_request(track)
        await message.channel.send(response)
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.command(name='ping', help='Pings the bot, returns latency. Why? ¯\_(ツ)_/¯')
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(f'latency {latency}')

@bot.command(name='play', aliases=['p'], help='tracks action of play message when rythm bot is active')
async def play(ctx):
    await ctx.send("I'm listening. But I'm not cool yet.")

bot.run(TOKEN)
