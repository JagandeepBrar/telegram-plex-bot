from backend import constants, logger
from backend.api import radarr, sonarr
from backend.database.statement import select
from backend.scheduler.tasks import catalogue

import telegram
import datetime

def notifyImmediately(bot, job):
    # Pulls the watch_id, and decodes the bytes back to the data
    try:
        watch_id = job.context.decode('utf-8')
        data = watch_id.split(";")
    except:
        logger.error(__name__, "notifyImmediately() failed to extract and process watch_id")
        return True
    # If the media isn't in the database, refreshes the databases first
    if(int(data[1]) == constants.NOTIFIER_MEDIA_TYPE_MOVIE and select.getMovie(data[0]) == None and radarr.enabled):
        catalogue.updateMovies(None, None)
    elif(int(data[1]) == constants.NOTIFIER_MEDIA_TYPE_TELEVISION and select.getShow(data[0]) == None and sonarr.enabled):
        catalogue.updateTelevision(None, None)
    # Gets the metadata for the movie and the list of users who need notifications
    metadata = select.getMetadata(watch_id, data[1])
    users = select.getUsersImmediateUpdate(data[0], data[1])
    # If there are no users watching this show or movie, print a log and return
    if(len(users) == 0):
        logger.info(__name__, "New content ({}): Notified no users".format(metadata[2]), "INFO_GREEN")
        return True
    # Build the messages
    if(int(data[1]) == constants.NOTIFIER_MEDIA_TYPE_TELEVISION):
        msg_simple = constants.NOTIFIER_IMMEDIATELY_HEADER + buildSimpleTelevisionMessage(metadata)
        msg_complex = constants.NOTIFIER_IMMEDIATELY_HEADER + buildComplexTelevisionMessage(metadata)
        is_upgrade = metadata[9]
    elif(int(data[1]) == constants.NOTIFIER_MEDIA_TYPE_MOVIE):
        msg_simple = constants.NOTIFIER_IMMEDIATELY_HEADER + buildSimpleMovieMessage(metadata)
        msg_complex = constants.NOTIFIER_IMMEDIATELY_HEADER + buildComplexMovieMessage(metadata)
        is_upgrade = metadata[5]
    # Process user messages
    notifications_counter = 0
    for user in users:
        user_data = select.getUser(user[0])
        # Checks if the user is banned or restricted
        if((not constants.RESTRICTED_NOTIFICATIONS or user_data[1] != constants.ACCOUNT_STATUS_RESTRICTED) and user_data[1] != constants.ACCOUNT_STATUS_BANNED):
            # Checks if the media was an upgrade
            if(is_upgrade == 1):
                if(user_data[3] == constants.ACCOUNT_UPGRADE_YES):
                    # Gets the complexity and sends the appropriate message
                    if(user_data[2] == constants.ACCOUNT_DETAIL_SIMPLE):
                        bot.send_message(chat_id=user_data[0], text=msg_simple, parse_mode=telegram.ParseMode.MARKDOWN)
                    elif(user_data[2]== constants.ACCOUNT_DETAIL_COMPLEX):
                        bot.send_message(chat_id=user_data[0], text=msg_complex, parse_mode=telegram.ParseMode.MARKDOWN)
                    notifications_counter += 1
            else:
                # Gets the complexity and sends the appropriate message
                if(user_data[2] == constants.ACCOUNT_DETAIL_SIMPLE):
                    bot.send_message(chat_id=user_data[0], text=msg_simple, parse_mode=telegram.ParseMode.MARKDOWN)
                elif(user_data[2]== constants.ACCOUNT_DETAIL_COMPLEX):
                    bot.send_message(chat_id=user_data[0], text=msg_complex, parse_mode=telegram.ParseMode.MARKDOWN)
                notifications_counter += 1
    logger.info(__name__, "New content ({}): notified {} user(s)".format(metadata[2], notifications_counter), "INFO_GREEN")

def notifyDaily(bot, job):
    users = select.getUsers()
    for user in users:
        # Gets the notifiers
        notifiers = select.getNotifiersForUserDaily(user[0], constants.NOTIFIER_MEDIA_TYPE_TELEVISION)
        # Makes sure the user has at least one TV notifier
        if(len(notifiers) != 0):
            # Builds the message
            msg = buildReportMessage(notifiers, constants.NOTIFIER_DAILY_HEADER, constants.NOTIFIER_FREQUENCY_DAILY)
            # Makes sure there is new content to notify the user about and send it if there is
            if(msg != constants.NOTIFIER_DAILY_HEADER):
                bot.send_message(chat_id=user[0], text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    logger.info(__name__, "Daily content report sent to all applicable users", "INFO_GREEN")

def notifyWeekly(bot, job):
    users = select.getUsers()
    for user in users:
        # Gets the notifiers
        notifiers = select.getNotifiersForUserWeekly(user[0], constants.NOTIFIER_MEDIA_TYPE_TELEVISION)
        # Makes sure the user has at least one TV notifier
        if(len(notifiers) != 0):
            # Builds the message
            msg = buildReportMessage(notifiers, constants.NOTIFIER_WEEKLY_HEADER, constants.NOTIFIER_FREQUENCY_WEEKLY)
            # Makes sure there is new content to notify the user about and send it if there is
            if(msg != constants.NOTIFIER_WEEKLY_HEADER):
                bot.send_message(chat_id=user[0], text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    logger.info(__name__, "Weekly content report sent to all applicable users", "INFO_GREEN")

# Returns a formatted string for some television metadata (simple format)
def buildSimpleTelevisionMessage(metadata):
    return "*{}*\nSeason {} Episode {}\n\n".format(metadata[2], metadata[5], metadata[6]) 

#Returns a formatted string for some television metadata (complex format)
def buildComplexTelevisionMessage(metadata):
    return "*{}*\nSeason {} Episode {}\n\"_{}_\"\n\n{} | {} | {}\n\n".format(metadata[2], metadata[5], metadata[6], metadata[4], metadata[3], metadata[7], constants.NOTIFIER_QUALITY_VERSIONS[int(metadata[8])])

# Returns a formatted string for some movie metadata (simple format)
def buildSimpleMovieMessage(metadata):
    return "*{}*".format(metadata[2])

# Returns a formatted string for some movie metadata (complex format)
def buildComplexMovieMessage(metadata):
    return "*{}*\n\n{} | {}".format(metadata[2], metadata[3], constants.NOTIFIER_QUALITY_VERSIONS[int(metadata[4])])

# Returns a formatted string for all new television for that day for a user's notifiers
def buildReportMessage(notifiers, header, timeframe):
    msg = header
    for notifier in notifiers:
        if(timeframe == constants.NOTIFIER_FREQUENCY_DAILY):
            metadata = select.getMetadataPastDay(constants.NOTIFIER_MEDIA_TYPE_TELEVISION, notifier[2], constants.ACCOUNT_UPGRADE_NO)
        elif(timeframe == constants.NOTIFIER_FREQUENCY_WEEKLY):
            metadata = select.getMetadataPastWeek(constants.NOTIFIER_MEDIA_TYPE_TELEVISION, notifier[2], constants.ACCOUNT_UPGRADE_NO)
        if(len(metadata) != 0):
            msg += "\n*{}*: {} new episode(s)".format(str(metadata[0][2]), len(metadata))
    return msg

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
        logger.error(__name__, "Invalid NOTIFICATION_TIME in backend/constants.py")
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
        logger.error(__name__, "Invalid NOTIFICATION_TIME or NOTIFICATION_DAY in backend/constants.py")
        exit()
    # Returns the total amount of seconds until the notification time
    return int(abs((now-notification_time).total_seconds()))