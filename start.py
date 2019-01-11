import backend.config as config
import backend.database.table as table
import backend.api.telegram as telegram
import backend.jobs.scheduler as scheduler

def start():
    # Initialize all the things
    config.initialize()
    table.initialize()
    scheduler.initialize()
    # If it got here, it means that everything has initialized correctly so the bot is about to start
    print("Download notifier has started!")
    telegram.updater.start_polling()
    telegram.updater.idle()

if(__name__ == "__main__"):
    start()
