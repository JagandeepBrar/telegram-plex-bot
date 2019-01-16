import backend.config as config
import backend.database.table as table
import backend.api.telegram as telegram
import backend.scheduler.jobs as jobs
import backend.commands.handlers as handlers
import backend.constants as constants
import logging
import sys

def start():
    # Initialize all the things
    config.initialize()
    table.initialize()
    handlers.initialize()
    jobs.initialize()
    # If it got here, it means that everything has initialized correctly so the bot is about to start
    logging.getLogger("start.main").info("{} ({}: @{}) has started!".format(constants.BOT_NAME, telegram.updater.bot.id, telegram.updater.bot.username))
    telegram.updater.start_polling()
    telegram.updater.idle()

if(__name__ == "__main__"):
    start()
