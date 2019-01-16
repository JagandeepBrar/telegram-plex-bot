import telegram
import logging
import backend.api.telegram

from backend import constants
from backend.scheduler.jobs import catalogue
from backend.commands import checker
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import select, insert

@send_typing_action
def forceUpdate(bot, update):
    catalogue.updateMovies(None, None)
    update.message.reply_text(constants.MOVIES_FORCEUPDATE, parse_mode=telegram.ParseMode.MARKDOWN)

@send_typing_action
def watchMovie(bot, update, args):
    if(checker.checkAllowed(update, constants.RESTRICTED_WATCHMOVIE)):
        if((len(args) == 0)):
            update.message.reply_text(constants.MOVIES_WATCH_EMPTY_ARGS, parse_mode=telegram.ParseMode.MARKDOWN)
            return True
        movie_search = select.getMoviesSearch(" ".join(args))
        if(len(movie_search) == 0):
            update.message.reply_text(constants.MOVIES_WATCH_EMPTY_SEARCH, parse_mode=telegram.ParseMode.MARKDOWN)
            return False
        keyboard = []
        for movie in range(min(10, len(movie_search))):
            keyboard.append([telegram.InlineKeyboardButton(movie_search[movie][1], callback_data=constants.MOVIES_WATCH_CALLBACK+movie_search[movie][1])])
        reply_markup = telegram.InlineKeyboardMarkup(keyboard)
        update.message.reply_text(constants.MOVIES_WATCH_FIRST_TEN, reply_markup=reply_markup, pass_chat_data=True, parse_mode=telegram.ParseMode.MARKDOWN)

def watchMovieCallback(bot, update):
    movie_name = update.callback_query.data[len(constants.MOVIES_WATCH_CALLBACK):]
    movie_id = select.getMovieByName(movie_name)[0]
    telegram_id = update.callback_query.message.chat_id
    telegram_name = update._effective_user.full_name
    watch_id = str(telegram_id)+str(constants.NOTIFIER_MEDIA_TYPE_MOVIE)+str(movie_id)
    desc = telegram_name + " monitoring " + movie_name

    insert.insertNotifier(watch_id, telegram_id, movie_id, constants.NOTIFIER_MEDIA_TYPE_MOVIE, desc)
    logging.getLogger(__name__).info("{} started monitoring a movie: {}".format(telegram_name, movie_name))
    bot.edit_message_text(text=constants.MOVIES_WATCH_SUCCESS.format(movie_name),chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, parse_mode=telegram.ParseMode.MARKDOWN)
