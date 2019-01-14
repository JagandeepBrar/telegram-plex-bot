import telegram
import logging
import backend.api.telegram

from backend import constants
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import insert, select, update as update_db

# Register the user (add to 'users' table in database)
@send_typing_action
def register(bot, update):
    if(backend.api.telegram.isAdmin(update.message.chat_id)):
        insert.insertUser(update.message.chat_id, update.message.from_user.full_name, constants.ACCOUNT_STATUS_ADMIN)
    else:
        insert.insertUser(update.message.chat_id, update.message.from_user.full_name, constants.ACCOUNT_STATUS_UNVERIFIED)
    user_status = select.getUser(update.message.chat_id)[2]
    logging.getLogger(__name__).info("User registered - {}: {}".format(update.message.chat_id, update.message.from_user.full_name))
    bot.send_message(chat_id=update.message.chat_id, text=constants.ACCOUNT_STATUS_MSG[user_status], parse_mode=telegram.ParseMode.MARKDOWN)

# Check the status of the asking user
@send_typing_action
def check(bot, update):
    register(bot, update)
