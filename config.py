import configparser
import logging
import codecs
import os
import csv

from json import loads

log = logging.getLogger(__name__)

CONFIG_FILE = "./data/config.ini"
config = configparser.ConfigParser()
config.read_file(codecs.open(CONFIG_FILE, "r+", "utf-8"))


def read_config(section, value, file="./data/config.ini"):
    config.read_file(codecs.open(file, "r+", "utf-8"))


# Bot section.

# TODO: Fix this.
# if bool(config.get("Bot", "token_env_var")):
#     BOT_TOKEN = os.getenv("zoidberg_token")
# else:
BOT_TOKEN = config.get("Bot", "bot_token")
CHANNELS = config.get("Bot", "channels")