import configparser
import sys

from colored import stylize
from backend import constants, logger
from backend.api import telegram, sonarr, radarr, ombi

parser = None

def initialize():
    initParser()
    parseConfig()

# Initialize the configuration parser
def initParser():
    global parser
    try:
        parser = configparser.ConfigParser()
        parser.read(constants.CONFIG_FILE)
        if not(len(parser) > 1):
            raise Exception()
        logger.info(__name__, "Configparser initialized")
    except:
        logger.error(__name__, "Failed to load config.ini: Please ensure that a valid config file is in the root directory")
        exit()

# Wrapper to parse all configuration data
def parseConfig():
    parseTelegram()
    parseOmbi()
    parseRadarr()
    parseSonarr()
    parseAdmins()
    parseNotifications()

def parseNotifications():
    try:
        if('NOTIFICATIONS' in parser):
            constants.NOTIFICATION_TIME = parser['NOTIFICATIONS']['TIME']
            constants.NOTIFICATION_DAY = parser['NOTIFICATIONS']['DAY']
            logger.warning(__name__, "Notification times set: {} @ {}".format(constants.NOTIFICATION_DAY, constants.NOTIFICATION_TIME))
        else:
            raise Exception()
    except:
        logger.error(__name__, "Failed to get notification times: Check your config.ini")
        exit()

# Admin list parsing
def parseAdmins():
    try:
        if('TELEGRAM' in parser):
            for admin in parser['TELEGRAM']['AUTO_ADMINS'].split(','):
                telegram.addAdmin(int(admin.strip()))
                logger.warning(__name__, "Telegram admins: {}".format(telegram.admins))
        else:
            raise Exception()
    except:
        logger.error(__name__, "Failed to get the admin user list: Check your config.ini")
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
            logger.info(__name__, "Sonarr API parsed")
    else:
        logger.error(__name__, "Could not read the Sonarr configuration values: Check your config.ini")
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
            logger.info(__name__, "Radarr API parsed")
    else:
        logger.error(__name__, "Could not read the Radarr configuration values: Check your config.ini")
        exit()

# Ombi API parsing
def parseOmbi():
    if('OMBI' in parser):
        if(parser.getboolean('OMBI', 'ENABLED')):
            ombi.enabled = True
            logger.info(__name__, "Ombi API parsed")
    else:
        logger.error(__name__, "Failed to initialize Ombi's API: Check your config.ini")
        exit()
    

# Telegram API parsing
def parseTelegram():
    if('TELEGRAM' in parser):
        telegram.api = parser['TELEGRAM']['BOT_TOKEN']
        telegram.auto_approve = parser.getboolean('TELEGRAM', 'AUTO_APPROVE')
        telegram.initialize()
        logger.info(__name__, "Telegram API initialized")
    else:
        logger.error(__name__, "Failed to initialize Telegram's API: Check your config.ini")
        exit()
