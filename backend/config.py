import configparser
import sys
import logging

from backend import constants
from backend.api import telegram, sonarr, radarr, ombi

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
    try:
        parser = configparser.ConfigParser()
        parser.read(constants.CONFIG_FILE)
        if not(len(parser) > 1):
            raise Exception()
        logger.info("Configparser initialized")
    except:
        logger.error("Failed to load config.ini. Please ensure that a valid config file is in the root directory.")
        exit()

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
        logger.error("Failed to get the admin user list. Check your config.ini.")
        exit()

# Sonarr API parsing
def parseSonarr():
    if('SONARR' in parser):
        if(parser.getboolean('SONARR', 'ENABLED')):
            sonarr.enabled = True
            sonarr.api = parser['SONARR']['API']
            sonarr.host = parser['SONARR']['HOST']
            sonarr.update_frequency = int(parser['SONARR']['UPDATE_FREQ'])
            sonarr.initialize()
            logger.info("Sonarr API parsed")
    else:
        logger.error("Could not read the Sonarr configuration values. Check your config.ini.")
        exit()

# Radarr API parsing
def parseRadarr():
    if('RADARR' in parser):
        if(parser.getboolean('RADARR', 'ENABLED')):
            radarr.enabled = True
            radarr.api = parser['RADARR']['API']
            radarr.host = parser['RADARR']['HOST']
            radarr.update_frequency = int(parser['RADARR']['UPDATE_FREQ'])
            radarr.initialize()
            logger.info("Radarr API parsed")
    else:
        logger.error("Could not read the Radarr configuration values. Check your config.ini.")
        exit()

# Ombi API parsing
def parseOmbi():
    if('OMBI' in parser):
        if(parser.getboolean('OMBI', 'ENABLED')):
            ombi.enabled = True
            logger.info("Ombi API parsed")
    else:
        logger.error("Failed to initialize Ombi's API. Check your config.ini.")
        exit()
    

# Telegram API parsing
def parseTelegram():
    if('TELEGRAM' in parser):
        telegram.api = parser['TELEGRAM']['BOT_TOKEN']
        telegram.auto_approve = parser.getboolean('TELEGRAM', 'AUTO_APPROVE')
        telegram.initialize()
        logger.info("Telegram API initialized")
    else:
        logger.error("Failed to initialize Telegram's API. Check your config.ini.")
        exit()
