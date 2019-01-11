from telegram.ext import Updater

api = None
updater = None
dispatcher = None

# Initialize the Telegram API
def initialize():
	global updater, dispatcher
	try:
		updater = Updater(token=api)
		dispatcher = updater.dispatcher
	except:
		raise Exception()