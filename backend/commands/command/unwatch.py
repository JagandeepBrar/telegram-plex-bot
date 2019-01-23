import telegram
import backend.api.telegram

from backend import constants, logger
from backend.api import sonarr, radarr
from backend.commands import checker
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import select, insert, delete
from backend.scheduler.jobs import catalogue

@send_typing_action
def unwatch(bot, update, args):
    if(checker.checkAllowed(update, constants.RESTRICTED_WATCHER_UNWATCH)):
        if(len(args) < 2):
            update.message.reply_text(constants.WATCHER_UNWATCH_EMPTY_ARGS, parse_mode=telegram.ParseMode.MARKDOWN)
            return False
        media_type = args[0].lower()
        if(media_type in constants.WATCHER_WATCH_SHOW_SYNONYMS and sonarr.enabled):
            return unwatchShow(bot, update, args[1:])
        if(media_type in constants.WATCHER_WATCH_MOVIE_SYNONYMS and radarr.enabled):
            return unwatchMovie(bot, update, args[1:])
        update.message.reply_text(constants.WATCHER_WATCH_INCORRECT_TYPE, parse_mode=telegram.ParseMode.MARKDOWN)


def unwatchShow(bot, update, args):
    show_search = select.getShowsWatchedSearch(update.message.chat_id, " ".join(args))
    if(len(show_search) == 0):
        update.message.reply_text(constants.TELEVISION_WATCH_EMPTY_SEARCH, parse_mode=telegram.ParseMode.MARKDOWN)
        return False
    keyboard = []
    for show in range(min(10, len(show_search))):
        keyboard.append([telegram.InlineKeyboardButton(show_search[show][1], callback_data=constants.TELEVISION_UNWATCH_CALLBACK+show_search[show][1])])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(constants.TELEVISION_WATCH_FIRST_TEN, reply_markup=reply_markup, pass_chat_data=True, parse_mode=telegram.ParseMode.MARKDOWN)

def unwatchShowCallback(bot, update):
    show_name = update.callback_query.data[len(constants.TELEVISION_UNWATCH_CALLBACK):]
    show_id = select.getShowByName(show_name)[0]
    telegram_id = update.callback_query.message.chat_id
    telegram_name = update._effective_user.full_name
    watch_id = str(telegram_id)+str(constants.NOTIFIER_MEDIA_TYPE_TELEVISION)+str(show_id)
    desc = telegram_name + " unwatched " + show_name

    delete.deleteNotifier(watch_id)
    logger.info(__name__, "{} unwatched a show: {}".format(telegram_name, show_name))
    bot.edit_message_text(text=constants.TELEVISION_UNWATCH_SUCCESS.format(show_name), chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, parse_mode=telegram.ParseMode.MARKDOWN)

def unwatchMovie(bot, update, args):
    movie_search = select.getMoviesWatchedSearch(update.message.chat_id, " ".join(args))
    if(len(movie_search) == 0):
        update.message.reply_text(constants.MOVIES_WATCH_EMPTY_SEARCH, parse_mode=telegram.ParseMode.MARKDOWN)
        return False
    keyboard = []
    for movie in range(min(10, len(movie_search))):
        keyboard.append([telegram.InlineKeyboardButton(movie_search[movie][1], callback_data=constants.MOVIES_UNWATCH_CALLBACK+movie_search[movie][1])])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(constants.MOVIES_WATCH_FIRST_TEN, reply_markup=reply_markup, pass_chat_data=True, parse_mode=telegram.ParseMode.MARKDOWN)

def unwatchMovieCallback(bot, update):
    movie_name = update.callback_query.data[len(constants.MOVIES_UNWATCH_CALLBACK):]
    movie_id = select.getMovieByName(movie_name)[0]
    telegram_id = update.callback_query.message.chat_id
    telegram_name = update._effective_user.full_name
    watch_id = str(telegram_id)+str(constants.NOTIFIER_MEDIA_TYPE_MOVIE)+str(movie_id)
    desc = telegram_name + " unwatched " + movie_name

    delete.deleteNotifier(watch_id)
    logger.info(__name__, "{} unwatched a show: {}".format(telegram_name, movie_name))
    bot.edit_message_text(text=constants.MOVIES_UNWATCH_SUCCESS.format(movie_name), chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, parse_mode=telegram.ParseMode.MARKDOWN)
