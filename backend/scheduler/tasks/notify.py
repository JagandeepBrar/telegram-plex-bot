from backend import constants
import logging
import datetime

def notifyImmediately(bot, job):
    pass

def notifyDaily(bot, job):
    pass

def notifyWeekly(bot, job):
    pass

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