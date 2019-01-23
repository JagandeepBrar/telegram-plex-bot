import telegram
import backend.api.telegram

from backend import constants, logger
from backend.api import sonarr, radarr
from backend.commands import checker
from backend.commands.command import movies, television
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import select, insert

@send_typing_action
def watch(bot, update, args):
    if(checker.checkAllowed(update, constants.RESTRICTED_WATCHER_WATCH)):
        if(len(args) < 2):
            update.message.reply_text(constants.WATCHER_WATCH_EMPTY_ARGS, parse_mode=telegram.ParseMode.MARKDOWN)
            return False
        media_type = args[0].lower()
        if(media_type in constants.WATCHER_WATCH_SHOW_SYNONYMS and sonarr.enabled):
            return television.watchShow(bot, update, args[1:])
        if(media_type in constants.WATCHER_WATCH_MOVIE_SYNONYMS and radarr.enabled):
            return movies.watchMovie(bot, update, args[1:])
        update.message.reply_text(constants.WATCHER_WATCH_INCORRECT_TYPE, parse_mode=telegram.ParseMode.MARKDOWN)

@send_typing_action
def unwatch(bot, update, args):
    if(checker.checkAllowed(update, constants.RESTRICTED_WATCHER_UNWATCH)):
        if(len(args) < 2):
            update.message.reply_text(constants.WATCHER_UNWATCH_EMPTY_ARGS, parse_mode=telegram.ParseMode.MARKDOWN)
            return False
        media_type = args[0].lower()
        if(media_type in constants.WATCHER_WATCH_SHOW_SYNONYMS and sonarr.enabled):
            return television.unwatchShow(bot, update, args[1:])
        if(media_type in constants.WATCHER_WATCH_MOVIE_SYNONYMS and radarr.enabled):
            return movies.unwatchMovie(bot, update, args[1:])
        update.message.reply_text(constants.WATCHER_WATCH_INCORRECT_TYPE, parse_mode=telegram.ParseMode.MARKDOWN)
