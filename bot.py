import discord
from discord.ext.commands import Bot, Context

from config import *

import csv

__version__ = get_string("VERSION")
logging.basicConfig(level=exec(LOGGING_LEVEL))

log = logging.getLogger(__name__)
bot = Bot(
    command_prefix='!'
)

bot.load_extension("cogs.confess")


@bot.listen()
async def on_ready():
    log.info(f"Bot is ready: logged in as {bot.user.name} ({bot.user.id})")

    await bot.wait_until_ready()


@bot.command(name="ping", brief="The bot responds if alive")
async def cmd_ping(ctx: Context):
    # Literally just responds with this.
    await ctx.send(f"Pong! :ping_pong:       Latency: {0} ms".format(bot.latency))


@bot.listen()
async def on_message(message):
    if message.channel in CHANNELS:
        append_message(message.content, message.author)        


def append_message(message, author):
    with open("messages.csv", 'a+', newline='') as writer:
        csv = writer(writer)
        csv.writerow([message, author])

bot.run(BOT_TOKEN)