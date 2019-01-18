import datetime

#############################
# APPLICATION CONFIGURATION #
#############################

CONFIG_FILE = "config.ini"
DB_FILE = "database.db"
BOT_NAME = "Plex Assistant"

################
# RESTRICTIONS #
################

RESTRICTED_WATCHER_WATCH = True
RESTRICTED_WATCHER_UNWATCH = True

#################
# API ENDPOINTS #
#################

SONARR_SYSTEM_STATUS = "system/status"
SONARR_SERIES = "/series"
SONARR_SERIES_LOOKUP = "/series/lookup?term=tvdb:"

RADARR_SYSTEM_STATUS = "system/status"
RADARR_MOVIES = "/movie"
RADARR_MOVIES_LOOKUP = "/movie/lookup/tmdb?tmdbId="

###########
# GENERAL #
###########

HOUR_IN_SECONDS = 3600
DAY_IN_SECONDS = HOUR_IN_SECONDS*24
WEEK_IN_SECONDS = DAY_IN_SECONDS*7

############################
# ACCOUNT COMMANDS RELATED #
############################

# ACCOUNT COMMAND OPTIONS

ACCOUNT_STATE_OPTIONS, ACCOUNT_STATE_OMBI, ACCOUNT_STATE_FREQ, ACCOUNT_STATE_DETAIL = range(4)
ACCOUNT_OPTIONS = ["Update Ombi ID", "Update Notification Frequency", "Update Notification Detail", "Exit"]
ACCOUNT_OPTIONS_REGEX = "^({}|{}|{}|{})$".format(ACCOUNT_OPTIONS[0], ACCOUNT_OPTIONS[1], ACCOUNT_OPTIONS[2], ACCOUNT_OPTIONS[3])

ACCOUNT_OPTIONS_REPLY_MARKUP = []
for opt in range(len(ACCOUNT_OPTIONS)):
    ACCOUNT_OPTIONS_REPLY_MARKUP.append([ACCOUNT_OPTIONS[opt]])

ACCOUNT_FREQ_UPDATED_MSG = "_Notification frequency has been updated._"
ACCOUNT_DETAIL_UPDATED_MSG = "_Notification detail has been updated._"
ACCOUNT_OMBI_UPDATED_MSG = "_Ombi ID has been updated._"
ACCOUNT_CLOSED_MSG = "_Account settings have been saved. Updated user information:_\n\n*Telegram ID:* {}\n*Status:* {}\n*Frequency:* {}\n*Notification Detail*: {}\n*Ombi ID:* {}\n*Name:* {}\n"

# ACCOUNT STATUS INCORRECT MESSAGES

ACCOUNT_UNAUTHORIZED = "_Sorry, this command can only be run by admins/owners._"
ACCOUNT_UNREGISTERED = "_Sorry, you are not registered._\n\nUse /register to get started!"
ACCOUNT_UNVERIFIED = "_Sorry, you are unverified._\n\nPlease wait for an admin/owner to verify your account."
ACCOUNT_RESTRICTED = "_Sorry, you are restricted._\n\nThis command can only be run by unrestricted accounts."
ACCOUNT_BANNED = "_Sorry, you are banned._\n\nThis command can only be run by unbanned accounts."

# ACCOUNT REGISTRATION 

ACCOUNT_REGISTER_STATE_FREQ, ACCOUNT_REGISTER_STATE_OMBI, ACCOUNT_REGISTER_STATE_DETAIL = range(3)
ACCOUNT_REGISTER_FREQ = "How frequently do you want to be notified on your monitored shows and movies?"
ACCOUNT_REGISTER_OMBI = "What is your Ombi ID? If you do not use Ombi, or can't remember, type /skip."
ACCOUNT_REGISTER_START = "Welcome to {}, let's get you registered so you can start using me!\n\n".format(BOT_NAME)+ACCOUNT_REGISTER_FREQ
ACCOUNT_REGISTER_DETAIL = "How much detail do you want in your notifications?"
ACCOUNT_REGISTER_FAIL_REGISTERED = "_Looks like you're already registered!_\n\nUse /account to get the current status of your account."
ACCOUNT_REGISTER_FAIL_CANCELLED = "_Registration has been cancelled._\n\nUse /register to start the registration process again."

# USER FREQUENCY LEVELS

ACCOUNT_FREQUENCY_IMMEDIATELY = 0
ACCOUNT_FREQUENCY_DAILY = 1
ACCOUNT_FREQUENCY_WEEKLY = 2
ACCOUNT_FREQUENCY = ["Immediately", "Daily", "Weekly"]
ACCOUNT_FREQUENCY_REGEX = "^({}|{}|{})$".format(ACCOUNT_FREQUENCY[0], ACCOUNT_FREQUENCY[1], ACCOUNT_FREQUENCY[2])

ACCOUNT_FREQUENCY_REPLY_MARKUP = []
for opt in range(len(ACCOUNT_FREQUENCY)):
    ACCOUNT_FREQUENCY_REPLY_MARKUP.append([ACCOUNT_FREQUENCY[opt]])

# USER DETAILED LEVELS

ACCOUNT_DETAIL_SIMPLE = 0
ACCOUNT_DETAIL_COMPLEX = 1
ACCOUNT_DETAIL = ["Simple", "Complex"]
ACCOUNT_DETAIL_REGEX = "^({}|{})$".format(ACCOUNT_DETAIL[0], ACCOUNT_DETAIL[1])

ACCOUNT_DETAIL_REPLY_MARKUP = []
for opt in range(len(ACCOUNT_DETAIL)):
    ACCOUNT_DETAIL_REPLY_MARKUP.append([ACCOUNT_DETAIL[opt]])

# USER ACCESS LEVELS
ACCOUNT_STATUS_ADMIN = 0
ACCOUNT_STATUS_UNVERIFIED = 1
ACCOUNT_STATUS_VERIFIED = 2
ACCOUNT_STATUS_RESTRICTED = 3
ACCOUNT_STATUS_BANNED = 4
ACCOUNT_STATUS = ["Admin", "Unverified", "Verified", "Restricted", "Banned"]

ACCOUNT_STATUS_REPLY_MARKUP = []
for opt in range(len(ACCOUNT_STATUS)):
    ACCOUNT_STATUS_REPLY_MARKUP.append([ACCOUNT_STATUS[opt]])

# USER STATUS MESSAGES
ACCOUNT_STATUS_ADMIN_MSG = "*You are registered as an admin/owner!*\n\nYou have full access to all commands, use /help to see all available commands."
ACCOUNT_STATUS_PENDING_MSG = "*You are registered!*\n\nYour account is pending verification, you will be notified when verification is complete."
ACCOUNT_STATUS_VERIFIED_MSG = "*You are registered and verified!*\n\nUse /help to see all available commands."
ACCOUNT_STATUS_RESTRICTED_MSG = "*You are verifed but restricted!*\n\nYour account is active, but your access is restricted. Please inquire with the admin(s)."
ACCOUNT_STATUS_BANNED_MSG = "*You are banned!*\n\nPlease inquire with the admins(s)."
ACCOUNT_STATUS_MSG = [ACCOUNT_STATUS_ADMIN_MSG, ACCOUNT_STATUS_PENDING_MSG, ACCOUNT_STATUS_VERIFIED_MSG, ACCOUNT_STATUS_RESTRICTED_MSG, ACCOUNT_STATUS_BANNED_MSG]

ACCOUNT_STATUS_FOOTER_MSG = "\n\nTap \"Exit\" or type /exit to exit account settings."

############################
# WATCHER COMMANDS RELATED #
############################

WATCHER_WATCH_EMPTY_ARGS =  "_/watch usage:_\n\n/watch <type> <name>"
WATCHER_WATCH_INCORRECT_TYPE = "_Sorry, that is not a valid type of media._"
WATCHER_WATCH_MOVIE_SYNONYMS = ['movie', 'movies', 'film']
WATCHER_WATCH_SHOW_SYNONYMS = ['show', 'television', 'series']

WATCHER_UNWATCH_EMPTY_ARGS = "_/unwatch usage:_\n\n/unwatch <type> <name>"

###############################
# TELEVISION COMMANDS RELATED #
###############################

TELEVISION_FORCEUPDATE = "_Television database has been updated._"

TELEVISION_WATCH_EMPTY_SEARCH = "_Sorry, no shows were found containing those words._"
TELEVISION_WATCH_FIRST_TEN = "_Here are the first ten results:_\n\nIf you cannot find the show, try making your search more specific."
TELEVISION_WATCH_SUCCESS = "_You are now watching_ *{}!*\n\nYou will be notified for any new episodes for this show according to your notification frequency preference."

TELEVISION_UNWATCH_SUCCESS = "_You have stopped watching_ *{}!*\n\nYou will no longer be notified for any new episodes."

###########################
# MOVIES COMMANDS RELATED #
###########################

MOVIES_FORCEUPDATE = "_Movies database has been updated._"

MOVIES_WATCH_EMPTY_SEARCH = "_Sorry, no movies were found containing those words._"
MOVIES_WATCH_FIRST_TEN = "_Here are the first ten results:_\n\nIf you cannot find the movie, try making your search more specific."
MOVIES_WATCH_SUCCESS = "_You are now watching_ *{}!*\n\nYou will be notified when this movie is available according to your notification frequency preference."

MOVIES_UNWATCH_SUCCESS = "_You have stopped watching *{}!*\n\nYou will no longer be notified when this movie is available."

#############################
# NOTIFIER COMMANDS RELATED #
#############################

NOTIFIER_MEDIA_TYPE_TELEVISION = 0
NOTIFIER_MEDIA_TYPE_MOVIE = 1
NOTIFIER_MEDIA_TYPE_MUSIC = 2

##########################
# ADMIN COMMANDS RELATED #
##########################

ADMIN_ACCESS_START_MSG = "_Please select the user access level:_"
ADMIN_ACCESS_USERS_MSG = "_Here is a list of users that are {}(s):_"
ADMIN_ACCESS_SET_MSG = "_What would you like to set this user's access level to?_"
ADMIN_ACCESS_SUCCESS = "_{}: {}'s access level has been updated to {}._"

ADMIN_FORCEUPDATE_FAILED_ARGS = "_/forceupdate usage:_\n\n/forceupdate <Database>"
ADMIN_FORCEUPDATE_FAILED_TYPE = "_The supplied database is not a valid database. Valid databases include:_\n\n- `shows`\n- `movies`\n- `all`"

####################
# HANDLER PREFIXES #
####################

ADMIN_ACCESS_TYPE_CALLBACK = "account_ACCESS_TYPE_"
ADMIN_ACCESS_USER_CALLBACK = "account_ACCESS_USER_"
ADMIN_ACCESS_SET_CALLBACK = "account_ACCESS_SET_"

TELEVISION_WATCH_CALLBACK = "television_WATCHSHOW_"
TELEVISION_UNWATCH_CALLBACK = "television_UNWATCHSHOW_"

MOVIES_WATCH_CALLBACK = "movie_WATCHMOVIE_"
MOVIES_UNWATCH_CALLBACK = "movie_UNWATCHMOVIE_"

###########
# METHODS #
###########

def hoursToSeconds(hours):
    return hours*HOUR_IN_SECONDS

def daysToSeconds(days):
    return days*DAY_IN_SECONDS

def weekInSeconds(week):
    return week*WEEK_IN_SECONDS

# Taken from https://www.geeksforgeeks.org/python-difference-two-lists/
def listDifference(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif