from backend import config, database
import api.telegram

def start():
    config.initialize()
    database.initialize()
    print("Download notifier has started!")
    api.telegram.telegram_updater.start_polling()
    api.telegram.telegram_updater.idle()

if(__name__ == "__main__"):
    start()
