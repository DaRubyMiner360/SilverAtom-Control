import discord
from discord.ext import commands
import os
import random
import asyncio
import replit

from pathlib import Path
import motor.motor_asyncio

import keep_alive

import cogs._json

from cogs._aternosapi import AternosAPI

headers_cookie = "ATERNOS_SEC_ityn6tb0n6d00000=shndl5ow81t00000; ATERNOS_LANGUAGE=en; ATERNOS_SESSION=YYkWYnNSlxmeeGBDSnQPCzlQ6ooYZtaSTVzSSy7kwPrux9gc0JKTFCwDWvdBZnExY6bz9GDq23nQ19Qv25XtCeWkjiFYedZFFDH4; ATERNOS_SERVER=CwNPaYK1z1T4V7Pm"
TOKEN = "YYkWYnNSlxmeeGBDSnQPCzlQ6ooYZtaSTVzSSy7kwPrux9gc0JKTFCwDWvdBZnExY6bz9GDq23nQ19Qv25XtCeWkjiFYedZFFDH4"
server = AternosAPI(headers_cookie, TOKEN, timeout = 10)

if os.path.exists(".env"):
    from dotenv import load_dotenv

    load_dotenv()

def get_prefix(client, message):
    data = cogs._json.read_json('prefixes')
    if not message.guild or not str(message.guild.id) in data or data[str(message.guild.id)] == "=":
        prefixes = ['+']

        if not message.guild:
            prefixes = ['++']

        return commands.when_mentioned_or(*prefixes)(client, message)
    return commands.when_mentioned_or(data[str(message.guild.id)])(client, message)


bot = discord.ext.commands.Bot(
    # Create a new bot
    command_prefix=get_prefix,  # Set the prefix
    description='A bot to start the SilverAtom SMP server',  # Set a description for the bot
    owner_id=595353331468075018,  # Your unique User ID
    case_insensitive=True  # Make the commands case insensitive
)

bot.server = server

# case_insensitive=True is used as the commands are case sensitive by default

_cogs = ['cogs.commands']

@bot.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

    bot.remove_command('help')
    # Removes the help command
    # Make sure to do this before loading the cogs
    for cog in _cogs:
        bot.load_extension(cog)
    return


# Start the server
keep_alive.keep_alive()

# Finally, login the bot
bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
