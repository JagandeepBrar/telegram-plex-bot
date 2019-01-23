import telegram

from backend import constants
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import select

@send_typing_action
def help(bot, update):
    user_status = int(select.getUser(update.message.chat_id)[1])
    msg = constants.HELP_MESSAGES[user_status]
    bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
