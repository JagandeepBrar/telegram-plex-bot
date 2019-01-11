import configparser
import sys
import logging

import api.telegram

logger = None
parser = None

def initialize():
    initLogger()
    initParser()
    parseConfig()

# Initialize the logger
def initLogger():
    global logger
    sys.excepthook = exceptionHandler
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    logger = logging.getLogger(__name__)

# Initialize the configuration parser
def initParser():
    global parser
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    if not(len(parser) > 1):
        raise Exception()

# Wrapper to parse all configuration data
def parseConfig():
    parseOmbi()
    parseRadarr()
    parseSonarr()
    parseTelegram()

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
            api.telegram.telegram_api = parser['TELEGRAM']['BOT_TOKEN']
            api.telegram.initialize()
        else:
            raise Exception()
    except:
        raise Exception("config::parseTelegram() - Failed to initialize Telegram's API. Check your config.ini.")

# Exception handler
def exceptionHandler(exception_type, exception, traceback):
	print("\nERROR: %s\n" % exception)
