import logging, os
from colored import stylize, fg
from backend import constants

def initialize():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    info(__name__, "Logging initialized")

def info(name, msg, colour="INFO"):
    if(os.name == 'nt'):
        logging.getLogger(name).info(msg)
    else:
        logging.getLogger(name).info(stylize(msg, constants.LOGGING_COLOURS.get(colour)))


def error(name, msg):
    if(os.name == 'nt'):
        logging.getLogger(name).error(msg)
    else:
        logging.getLogger(name).error(stylize(msg, constants.LOGGING_COLOURS.get("ERROR")))

def warning(name, msg):
    if(os.name == 'nt'):
        logging.getLogger(name).warning(msg)
    else:
        logging.getLogger(name).warning(stylize(msg, constants.LOGGING_COLOURS.get("WARNING")))
