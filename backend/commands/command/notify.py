import telegram

from backend import constants
from backend.database.statement import select
from backend.commands import checker
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action

@send_typing_action
def notifyShow(bot, update, args):
    if(checker.checkAllowed(update, constants.RESTRICTED_NOTIFYSHOW)):
        update.message.reply_text("We good", parse_mode=telegram.ParseMode.MARKDOWN)

@send_typing_action
def notifyMovie(bot, update, args):
    if(checker.checkAllowed(update, constants.RESTRICTED_NOTIFYMOVIE)):
        update.message.reply_text("We good", parse_mode=telegram.ParseMode.MARKDOWN)
