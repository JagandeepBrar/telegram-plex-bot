import telegram
import backend.api.telegram

from backend import constants
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import insert, select

# Register the user (add to 'users' table in database)
@send_typing_action
def register(bot, update):
    if(backend.api.telegram.isAdmin(update.message.chat_id)):
        insert.insertUser(update.message.chat_id, update.message.from_user.full_name, constants.USER_ACCESS_ADMIN)
    else:
        insert.insertUser(update.message.chat_id, update.message.from_user.full_name, constants.USER_ACCESS_UNVERIFIED)
    user_status = select.getUser(update.message.chat_id)[2]
    bot.send_message(chat_id=update.message.chat_id, text=constants.STATUSES[user_status], parse_mode=telegram.ParseMode.MARKDOWN)

# Check the status of the asking user
@send_typing_action
def check(bot, update):
    register(bot, update)

def get_status(bot, update):
    pass

def set_status(bot, update):
    if(update.message.chat_id in select.getAdmins()):
        pass