import backend.config as config
import backend.database.table as db_table
import backend.api.telegram as telegram

def start():
    config.initialize()
    db_table.initialize()
    print("Download notifier has started!")
    telegram.telegram_updater.start_polling()
    telegram.telegram_updater.idle()

if(__name__ == "__main__"):
    start()
