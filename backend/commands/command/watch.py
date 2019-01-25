import telegram
import backend.api.telegram

from backend import constants, logger
from backend.api import sonarr, radarr
from backend.commands import checker
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import select, insert, update as update_db
from backend.scheduler.jobs import catalogue

@send_typing_action
def watch(bot, update, args):
    if(checker.checkAllowed(update, constants.RESTRICTED_WATCHER_WATCH)):
        if(len(args) < 2):
            update.message.reply_text(constants.WATCH_EMPTY_ARGS, parse_mode=telegram.ParseMode.MARKDOWN)
            return False
        media_type = args[0].lower()
        if(media_type in constants.SHOW_SYNONYMS and sonarr.enabled):
            return show(bot, update, args[1:])
        if(media_type in constants.MOVIE_SYNONYMS and radarr.enabled):
            return movie(bot, update, args[1:])
        update.message.reply_text(constants.WATCH_INCORRECT_TYPE, parse_mode=telegram.ParseMode.MARKDOWN)


def show(bot, update, args):
    show_search = select.getShowsSearch(" ".join(args))
    if(len(show_search) == 0):
        update.message.reply_text(constants.WATCH_TELEVISION_EMPTY_SEARCH, parse_mode=telegram.ParseMode.MARKDOWN)
        return False
    keyboard = []
    for show in range(min(10, len(show_search))):
        keyboard.append([telegram.InlineKeyboardButton(show_search[show][1], callback_data=constants.WATCH_TELEVISION_CALLBACK+show_search[show][1])])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(constants.WATCH_TELEVISION_FIRST_TEN, reply_markup=reply_markup, pass_chat_data=True, parse_mode=telegram.ParseMode.MARKDOWN)

def showSearch(bot, update):
    show_name = update.callback_query.data[len(constants.WATCH_TELEVISION_CALLBACK):]
    show_id = select.getShowByName(show_name)[0]
    telegram_id = update.callback_query.message.chat_id
    telegram_name = update._effective_user.full_name
    watch_id = str(telegram_id)+str(constants.NOTIFIER_MEDIA_TYPE_TELEVISION)+str(show_id)
    desc = telegram_name + " watching " + show_name

    insert.insertNotifier(watch_id, telegram_id, show_id, constants.NOTIFIER_MEDIA_TYPE_TELEVISION, constants.NOTIFIER_FREQUENCY_IMMEDIATELY, desc)
    logger.info(__name__, "{} started watching a show: {}".format(telegram_name, show_name))
    
    keyboard = []
    for freq in range(len(constants.NOTIFIER_FREQUENCY)):
        keyboard.append([telegram.InlineKeyboardButton(constants.NOTIFIER_FREQUENCY[freq], callback_data=constants.WATCH_TELEVISION_FREQ_CALLBACK+str(watch_id)+","+str(freq))])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(text=constants.WATCH_TELEVISION_FREQUENCY, reply_markup=reply_markup, chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, parse_mode=telegram.ParseMode.MARKDOWN)

def showFreq(bot, update):
    results =  update.callback_query.data[len(constants.WATCH_TELEVISION_FREQ_CALLBACK):].split(",")
    frequency = constants.NOTIFIER_FREQUENCY[int(results[1])].lower()
    show_name = select.getShow(select.getNotifier(results[0])[2])[1]
    update_db.updateNotifierFrequency(results[0], results[1])
    bot.edit_message_text(text=constants.WATCH_TELEVISION_SUCCESS.format(show_name, frequency), chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, parse_mode=telegram.ParseMode.MARKDOWN)

def movie(bot, update, args):
    movie_search = select.getMoviesSearch(" ".join(args))
    if(len(movie_search) == 0):
        update.message.reply_text(constants.WATCH_MOVIES_EMPTY_SEARCH, parse_mode=telegram.ParseMode.MARKDOWN)
        return False
    keyboard = []
    for movie in range(min(10, len(movie_search))):
        keyboard.append([telegram.InlineKeyboardButton(movie_search[movie][1], callback_data=constants.WATCH_MOVIE_CALLBACK+movie_search[movie][1])])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(constants.WATCH_MOVIES_FIRST_TEN, reply_markup=reply_markup, pass_chat_data=True, parse_mode=telegram.ParseMode.MARKDOWN)

def movieSearch(bot, update):
    movie_name = update.callback_query.data[len(constants.WATCH_MOVIE_CALLBACK):]
    movie_id = select.getMovieByName(movie_name)[0]
    telegram_id = update.callback_query.message.chat_id
    telegram_name = update._effective_user.full_name
    watch_id = str(telegram_id)+str(constants.NOTIFIER_MEDIA_TYPE_MOVIE)+str(movie_id)
    desc = telegram_name + " watching " + movie_name

    insert.insertNotifier(watch_id, telegram_id, movie_id, constants.NOTIFIER_MEDIA_TYPE_MOVIE, constants.NOTIFIER_FREQUENCY_IMMEDIATELY, desc)
    logger.info(__name__, "{} started watching a movie: {}".format(telegram_name, movie_name))
    bot.edit_message_text(text=constants.WATCH_MOVIES_SUCCESS.format(movie_name),chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, parse_mode=telegram.ParseMode.MARKDOWN)
