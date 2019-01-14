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
    logger = logging.getLogger(__name__)
    logger.info("Logger initialized")

# Initialize the configuration parser
def initParser():
    global parser
    parser = configparser.ConfigParser()
    parser.read(constants.CONFIG_FILE)
    if not(len(parser) > 1):
        raise Exception()
    logger.info("Configparser initialized")

# Wrapper to parse all configuration data
def parseConfig():
    parseTelegram()
    parseOmbi()
    parseRadarr()
    parseSonarr()
    parseAdmins()

# Admin list parsing
def parseAdmins():
    try:
        if('TELEGRAM' in parser):
            for admin in parser['TELEGRAM']['AUTO_ADMINS'].split(','):
                telegram.addAdmin(int(admin.strip()))
                logger.info("Telegram admins parsed {}".format(telegram.admins))
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
            logger.info("Telegram API initialized")
        else:
            raise Exception()
    except:
        raise Exception("config::parseTelegram() - Failed to initialize Telegram's API. Check your config.ini.")
