from backend import config, constants, logger
from backend.database import table
from backend.api import telegram
from backend.scheduler import jobs, server
from backend.commands import handlers

import sys
import atexit

def start():
    # Initialize all the things
    logger.initialize()
    config.initialize()
    table.initialize()
    handlers.initialize()
    jobs.initialize()
    server.initialize()
    # If it got here, it means that everything has initialized correctly so the bot is about to start
    logger.warning("main.start", "{} ({}: @{}) has started!".format(constants.BOT_NAME, telegram.updater.bot.id, telegram.updater.bot.username))
    telegram.updater.start_polling()
    telegram.updater.idle()

@atexit.register
def exit():
    server.stopServer()
    logger.warning("main.start", "Successfully closed {}!".format(constants.BOT_NAME))

if(__name__ == "__main__"):
    start()
