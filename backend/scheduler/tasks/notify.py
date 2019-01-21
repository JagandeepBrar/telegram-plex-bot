from backend import constants
from backend.database.statement import select
import telegram
import logging
import datetime

def notifyImmediately(bot, job):
    # Pulls the watch_id, and decodes the bytes back to the data
    logger = logging.getLogger(__name__)
    try:
        watch_id = job.context.decode('utf-8')
        data = watch_id.split(";")
    except:
        logger.error("notifyImmediately() failed to extract and process watch_id")
        return True
    # Gets the metadata for the movie and the list of users who need notifications
    metadata = select.getMetadata(watch_id, data[1])
    users = select.getUsersImmediateUpdate(data[0])
    # If there are no users watching this show, print a log and return
    if(len(users) == 0):
        logger.info("New content ({}): Notified no users".format(metadata[2]))
        return True
    # Build the messages
    if(int(data[1]) == constants.NOTIFIER_MEDIA_TYPE_TELEVISION):
        msg_simple = constants.NOTIFIER_IMMEDIATELY_HEADER + buildSimpleTelevisionMessage(metadata)
        msg_complex = constants.NOTIFIER_IMMEDIATELY_HEADER + buildComplexTelevisionMessage(metadata)
    else:
        msg_simple = constants.NOTIFIER_IMMEDIATELY_HEADER + buildSimpleMovieMessage(metadata)
        msg_complex = constants.NOTIFIER_IMMEDIATELY_HEADER + buildComplexMovieMessage(metadata)
    # Process user messages
    for user in users:
        user_data = select.getUser(user[0])
        # Checks if the user is banned or restricted
        if(user_data[1] != constants.ACCOUNT_BANNED or user_data[1] != constants.ACCOUNT_RESTRICTED):
            # Gets the complexity and sends the appropriate message
            if(user_data[2] == constants.ACCOUNT_DETAIL_SIMPLE):
                bot.send_message(chat_id=user_data[0], text=msg_simple, parse_mode=telegram.ParseMode.MARKDOWN)
            else:
                bot.send_message(chat_id=user_data[0], text=msg_complex, parse_mode=telegram.ParseMode.MARKDOWN)
    logger.info("New content ({}): notified {} user(s)".format(metadata[2], len(users)))

def notifyDaily(bot, job):
    pass

def notifyWeekly(bot, job):
    pass

def buildSimpleTelevisionMessage(metadata):
    return "*{}*\nSeason {} Episode {}".format(metadata[2], metadata[5], metadata[6]) 

def buildComplexTelevisionMessage(metadata):
    return "*{}*\nSeason {} Episode {}\n\"_{}_\"\n\n*Type:* {}\n*Quality:* {}\n*Version:* {}".format(metadata[2], metadata[5], metadata[6], metadata[4], metadata[3], metadata[7], constants.NOTIFIER_QUALITY_VERSIONS[int(metadata[8])])

def buildSimpleMovieMessage(metadata):
    return "simple"

def buildComplexMovieMessage(metadata):
    return "complex"


# Calculates the amount of seconds until the time to send the daily notification
# Will be off by -1 to -5 seconds, but it's close enough that it's negligible
def secondsToDaily():
    now = datetime.datetime.now()
    try:
        time = constants.NOTIFICATION_TIME.split(":")
        # If it's still the same day but past the notification time, adds a day
        if(now.hour >= int(time[0]) and now.minute >= int(time[1])):
            notification_time = datetime.datetime(now.year, now.month, now.day+1, int(time[0]), int(time[1]))
        else:
            notification_time = datetime.datetime(now.year, now.month, now.day, int(time[0]), int(time[1]))
    except:
        logging.getLogger(__name__).error("Invalid NOTIFICATION_TIME in backend/constants.py")
        exit()
    # Returns the total amount of seconds until the notification time
    return int(abs((now-notification_time).total_seconds()))

# Calculates the amount of seconds until the time to send the weekly notification
# Will be off by -1 to -5 seconds, but it's close enough that it's negligible
def secondsToWeekly():
    now = datetime.datetime.now()
    try:
        time = constants.NOTIFICATION_TIME.split(":")
        day = constants.WEEKDAYS.index(constants.NOTIFICATION_DAY)
        if(now.hour >= int(time[0]) and now.minute >= int(time[1])):
            # If it's still the same day but past the notification time, adds a day
            notification_time = datetime.datetime(now.year, now.month, now.day+1, int(time[0]), int(time[1]))
        else:
            notification_time = datetime.datetime(now.year, now.month, now.day, int(time[0]), int(time[1]))
        # Adds days to the notification time until it reaches the correct day
        while notification_time.weekday() != day:
            notification_time += datetime.timedelta(days=1)
    except:
        logging.getLogger(__name__).error("Invalid NOTIFICATION_TIME or NOTIFICATION_DAY in backend/constants.py")
        exit()
    # Returns the total amount of seconds until the notification time
    return int(abs((now-notification_time).total_seconds()))