from telegram.ext import Updater

admins = []
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

# Adds a telegram ID to the list of admins
def addAdmin(id):
    if(isinstance(id, int)):
        admins.append(id)

# Checks if <id> is in the admins list, returns accordingly
def isAdmin(id):
    if(isinstance(id, int)):
        if(id in admins):
            return True
    return False
