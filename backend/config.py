import configparser
import sys
import logging

from backend import constants
from backend.api import telegram

logger = None
parser = None

def initialize():
    initLogger()
    initParser()
    parseConfig()

# Initialize the logger
def initLogger():
    global logger
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    logger = logging.getLogger()

# Initialize the configuration parser
def initParser():
    global parser
    parser = configparser.ConfigParser()
    parser.read(constants.CONFIG_FILE)
    if not(len(parser) > 1):
        raise Exception()

# Wrapper to parse all configuration data
def parseConfig():
    parseAdmins()
    parseOmbi()
    parseRadarr()
    parseSonarr()
    parseTelegram()

# Admin list parsing
def parseAdmins():
    try:
        if('TELEGRAM' in parser):
            for admin in parser['TELEGRAM']['AUTO_ADMINS'].split(','):
                telegram.addAdmin(int(admin.strip()))
        else:
            raise Exception()
    except:
        raise Exception("config::parseAdmins() - Failed to get the admin user list. Check your config.ini.")

# Sonarr API parsing
def parseSonarr():
    pass

# Radarr API parsing
def parseRadarr():
    pass

# Ombi API parsing
def parseOmbi():
    pass

# Telegram API parsing
def parseTelegram():
    try:
        if('TELEGRAM' in parser):
            telegram.api = parser['TELEGRAM']['BOT_TOKEN']
            telegram.initialize()
        else:
            raise Exception()
    except:
        raise Exception("config::parseTelegram() - Failed to initialize Telegram's API. Check your config.ini.")
