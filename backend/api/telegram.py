from telegram.ext import Updater

telegram_api = None
telegram_updater = None
telegram_dispatcher = None

# Initialize the Telegram API
def initialize():
	global telegram_updater, telegram_dispatcher
	try:
		telegram_updater = Updater(token=telegram_api)
		telegram_dispatcher = telegram_updater.dispatcher
	except:
		raise Exception()