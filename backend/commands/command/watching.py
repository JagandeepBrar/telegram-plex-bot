import telegram
import backend.api.telegram

from backend import constants
from backend.commands import checker
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import select

@send_typing_action
def watching(bot, update):
    if(checker.checkAllowed(update, constants.RESTRICTED_WATCHER_WATCHING)):
        msg = ""
        # Get the notifiers
        notifiers_tv = select.getTelevisionNotifiersForUser(update.message.chat_id)
        notifiers_movies = select.getMoviesNotifiersForUser(update.message.chat_id)
        # Only build the TV list if there are shows being watched
        if(len(notifiers_tv) != 0):
            msg += constants.WATCHING_TELEVISION_HEADER
            for tv in notifiers_tv:
                msg += "*{}*\n".format(select.getShow(tv[2])[1])
            msg += "\n"
        # Only build the movie list if there are movies being watched
        if(len(notifiers_movies) != 0):
            msg += constants.WATCHING_MOVIE_HEADER
            for movie in notifiers_movies:
                msg += "*{}*\n".format(select.getMovie(movie[2])[1])
        # Print a general message if they aren't watching any content
        if(msg == ""):
            msg = constants.WATCHING_NO_CONTENT
        update.message.reply_text(msg, parse_mode=telegram.ParseMode.MARKDOWN)