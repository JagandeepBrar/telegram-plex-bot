import telegram
import logging
import backend.api.telegram

from backend import constants
from backend.scheduler.jobs import catalogue
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action

@send_typing_action
def forceUpdate(bot, update):
    catalogue.updateMovies(None, None)
    update.message.reply_text(constants.MOVIES_FORCEUPDATE, parse_mode=telegram.ParseMode.MARKDOWN)
