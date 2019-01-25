import telegram

from backend import constants
from backend.api import radarr, sonarr
from backend.scheduler.jobs import catalogue
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.commands import checker

@send_typing_action
def forceupdate(bot, update, args):
    if(checker.checkAdminAllowed(update)):
        if(len(args) == 1):
            if(args[0].lower() in constants.SHOW_SYNONYMS and sonarr.enabled):
                shows(bot, update)
            elif(args[0].lower() in constants.MOVIE_SYNONYMS and radarr.enabled):
                movies(bot, update)
            elif(args[0].lower() == "all"):
                if(sonarr.enabled):
                    shows(bot, update)
                if(radarr.enabled):
                    movies(bot, update)
            else:
                update.message.reply_text(constants.FORCEUPDATE_FAILED_TYPE, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            update.message.reply_text(constants.FORCEUPDATE_FAILED_ARGS, parse_mode=telegram.ParseMode.MARKDOWN)

@send_typing_action
def movies(bot, update):
    catalogue.updateMovies(None, None)
    update.message.reply_text(constants.FORCEUPDATE_MOVIES, parse_mode=telegram.ParseMode.MARKDOWN)

@send_typing_action
def shows(bot, update):
    catalogue.updateTelevision(None, None)
    update.message.reply_text(constants.FORCEUPDATE_TELEVISION, parse_mode=telegram.ParseMode.MARKDOWN)
