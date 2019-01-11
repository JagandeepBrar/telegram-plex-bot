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

def initLogger():
    global logger
    sys.excepthook = exceptionHandler
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    logger = logging.getLogger(__name__)

def initParser():
    global parser
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    if not(len(parser) > 1):
        raise Exception()

def parseConfig():
    parseSonarr()
    parseTelegram()

def parseSonarr():
    pass

def parseTelegram():
    try:
        if('TELEGRAM' in parser):
            api.telegram.telegram_api = parser['TELEGRAM']['BOT_TOKEN']
            api.telegram.initialize()
        else:
            raise Exception()
    except:
        raise Exception("config::parseTelegram() - Failed to initialize Telegram's API. Check your config.ini.")

def exceptionHandler(exception_type, exception, traceback):
	print("\nERROR: %s\n" % exception)
