import colored

################################
# COMMAND RESTRICTION SETTINGS #
################################

RESTRICTED_NOTIFICATIONS = True
RESTRICTED_WATCHER_WATCH = True
RESTRICTED_WATCHER_UNWATCH = True

###########
# GENERAL #
###########

MOVIE_SYNONYMS = ['movie', 'movies', 'film', 'cinema', 'short']
SHOW_SYNONYMS = ['show', 'shows', 'tv', 'television', 'series', 'miniseries', 'cartoon', 'anime', 'ova']
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MINUTE_IN_SECONDS = 60
HOUR_IN_SECONDS = MINUTE_IN_SECONDS*60
DAY_IN_SECONDS = HOUR_IN_SECONDS*24
WEEK_IN_SECONDS = DAY_IN_SECONDS*7

#############################
# APPLICATION CONFIGURATION #
#############################

CONFIG_FILE = "data/config.ini"
DB_FILE = "data/database.db"
BOT_NAME = "Plex Assistant"

NOTIFICATION_TIME = ""
NOTIFICATION_DAY = ""

###################
# LOGGING RELATED #
###################

LOGGING_COLOURS = {
    'INFO': colored.fg('white'), 
    'INFO_GREEN': colored.fg('white')+colored.bg('dark_green'),
    'INFO_BLUE': colored.fg('white')+colored.bg('deep_sky_blue_4c'),
    'WARNING': colored.fg('white')+colored.bg('orange_3'),
    'ERROR': colored.fg('white')+colored.bg('red'),
}

##################
# SOCKET RELATED #
##################

SOCKET_MAX_MSG_LENGTH = 256
SOCKET_HOST = "0.0.0.0"
SOCKET_PORT = "25535"

#################
# API ENDPOINTS #
#################

RADARR_SYSTEM_STATUS = "/api/system/status"
RADARR_MOVIES = "/api/movie"
RADARR_MOVIES_LOOKUP = "/api/movie/lookup/tmdb"
SONARR_SYSTEM_STATUS = "/api/system/status"
SONARR_SERIES = "/api/series"
SONARR_SERIES_LOOKUP = "/api/series/lookup"
OMBI_SYSTEM_STATUS = "/api/v1/Status/"

####################
# CHECKER MESSAGES #
####################

CHECKER_UNAUTHORIZED_MSG = "_Sorry, this command can only be run by the admin(s)._"
CHECKER_UNREGISTERED_MSG = "_Sorry, you are not registered._\n\nUse /register to get started!"
CHECKER_UNVERIFIED_MSG = "_Sorry, you are unverified._\n\nPlease wait for an admin to verify your account."
CHECKER_RESTRICTED_MSG = "_Sorry, you are restricted._\n\nThis command can only be run by unrestricted accounts."
CHECKER_BANNED_MSG = "_Sorry, you are banned._\n\nThis command can only be run by unbanned accounts."

###################
# ACCOUNT RELATED #
###################

ACCOUNT_DETAIL_SIMPLE = 0
ACCOUNT_DETAIL_COMPLEX = 1
ACCOUNT_DETAIL = ["Simple", "Complex"]
ACCOUNT_DETAIL_REGEX = "^({}|{})$".format(ACCOUNT_DETAIL[0], ACCOUNT_DETAIL[1])
ACCOUNT_DETAIL_REPLY_MARKUP = []
ACCOUNT_STATUS_ADMIN = 0
ACCOUNT_STATUS_UNVERIFIED = 1
ACCOUNT_STATUS_VERIFIED = 2
ACCOUNT_STATUS_RESTRICTED = 3
ACCOUNT_STATUS_BANNED = 4
ACCOUNT_STATUS = ["Admin", "Unverified", "Verified", "Restricted", "Banned"]
ACCOUNT_STATUS_REPLY_MARKUP = []
ACCOUNT_UPGRADE_NO = 0
ACCOUNT_UPGRADE_YES = 1
ACCOUNT_UPGRADE = ["No", "Yes"]
ACCOUNT_UPGRADE_REGEX = "^({}|{})$".format(ACCOUNT_UPGRADE[0], ACCOUNT_UPGRADE[1])
ACCOUNT_UPGRADE_REPLY_MARKUP = []


####################
# /ACCOUNT COMMAND #
####################

ACCOUNT_DETAIL_UPDATED_MSG = "_Notification detail has been updated._"
ACCOUNT_OMBI_UPDATED_MSG = "_Ombi ID has been updated._"
ACCOUNT_UPGRADE_UPDATED_MSG = "_Upgrade preference has been updated._"
ACCOUNT_CLOSED_MSG = "_Account settings have been saved. Updated user information:_\n\n*Telegram ID:* {}\n*Status:* {}\n*Notification Detail*: {}\n*Upgrade Notifications:* {}\n*Ombi ID:* {}\n*Name:* {}\n"
ACCOUNT_STATE_OPTIONS, ACCOUNT_STATE_OMBI, ACCOUNT_STATE_DETAIL, ACCOUNT_STATE_UPGRADE = range(4)
ACCOUNT_OPTIONS = ["Update Ombi ID", "Update Notification Detail", "Update Upgrade Preference", "Exit"]
ACCOUNT_OPTIONS_REGEX = "^({}|{}|{}|{})$".format(ACCOUNT_OPTIONS[0], ACCOUNT_OPTIONS[1], ACCOUNT_OPTIONS[2], ACCOUNT_OPTIONS[3])
ACCOUNT_OPTIONS_REPLY_MARKUP = []
ACCOUNT_STATUS_ADMIN_MSG = "*You are registered as an admin!*\n\nYou have full access to all commands, use /help to see all available commands."
ACCOUNT_STATUS_PENDING_MSG = "*You are registered!*\n\nYour account is pending verification, you will be notified when verification is complete."
ACCOUNT_STATUS_VERIFIED_MSG = "*You are registered and verified!*\n\nUse /help to see all available commands."
ACCOUNT_STATUS_RESTRICTED_MSG = "*You are verifed but restricted!*\n\nYour account is active, but your access is restricted. Please inquire with the admin(s)."
ACCOUNT_STATUS_BANNED_MSG = "*You are banned!*\n\nPlease inquire with the admin(s)."
ACCOUNT_STATUS_MSG = [ACCOUNT_STATUS_ADMIN_MSG, ACCOUNT_STATUS_PENDING_MSG, ACCOUNT_STATUS_VERIFIED_MSG, ACCOUNT_STATUS_RESTRICTED_MSG, ACCOUNT_STATUS_BANNED_MSG]
ACCOUNT_STATUS_FOOTER_MSG = "\n\nTap \"Exit\" or type /exit to exit account settings."

###################
# /ACCESS COMMAND #
###################

ACCESS_START_MSG = "_Please select the user access level:_"
ACCESS_USERS_MSG = "_Here is a list of users that are {}(s):_"
ACCESS_SET_MSG = "_What would you like to set this user's access level to?_"
ACCESS_SUCCESS = "_{}: {}'s access level has been updated to {}._"
ACCESS_GETSTATUS_CALLBACK = "access_GETSTATUS_"
ACCESS_USER_CALLBACK = "access_USER_"
ACCESS_SETSTATUS_CALLBACK = "access_SETSTATUS_"

##########################
# /DELETEACCOUNT COMMAND #
##########################

DELETEACCOUNT_STATE_OPTIONS = range(1)
DELETEACCOUNT_UNAUTHORIZED = "_Looks like you are restricted or banned._\n\nIn order to reduce abuse, we do not let accounts with these status to delete their account. Please inquire with the admin(s)."
DELETEACCOUNT_CONFIRM = "_Are you sure you want to delete your account?_\n\nThis will remove all of your watchers and account information from the bot. If you re-register, you will have to be verified again."
DELETEACCOUNT_SUCCESS = "_Your account details and watchers have been deleted._"
DELETEACCOUNT_CANCEL = "_Account deletion cancelled._"
DELETEACCOUNT_OPTIONS = ["Delete Account", "Cancel"]
DELETEACCOUNT_OPTIONS_REGEX = "^({}|{})$".format(DELETEACCOUNT_OPTIONS[0], DELETEACCOUNT_OPTIONS[1])
DELETEACCOUNT_OPTIONS_MARKUP = []

########################
# /FORCEUPDATE COMMAND #
########################

FORCEUPDATE_TELEVISION = "_Television database has been updated._"
FORCEUPDATE_MOVIES = "_Movies database has been updated._"
FORCEUPDATE_FAILED_ARGS = "_/forceupdate usage:_\n\n/forceupdate <Database>"
FORCEUPDATE_FAILED_TYPE = "_The supplied database is not a valid database._"

#################
# /HELP COMMAND #
#################

HELP_VERIFIED = """_User Commands:_

/account: View the status of your account, and update user preferences.
/deleteaccount: Deletes all of your account data from the bot, including all watchers.

/watch: Monitor some media for new content.
/unwatch: Unmonitor some media to stop being notified of new content.
"""
HELP_ADMIN = """_Admin Commands:_

/access: View and change user's status levels.
/forceupdate: Forcibly update the database of media.

"""+HELP_VERIFIED
HELP_UNVERIFIED = "_Your account is unverified._\n\nYour account must be verified before you can see the commands available."
HELP_RESTRICTED = HELP_VERIFIED
HELP_BANNED = "_Your account is banned._\n\nYou cannot run any commands."
HELP_MESSAGES = [HELP_ADMIN, HELP_UNVERIFIED, HELP_VERIFIED, HELP_RESTRICTED, HELP_BANNED]

#####################
# /REGISTER COMMAND #
#####################

ACCOUNT_REGISTER_STATE_OMBI, ACCOUNT_REGISTER_STATE_DETAIL, ACCOUNT_REGISTER_STATE_UPGRADE = range(3)
ACCOUNT_REGISTER_OMBI = "What is your Ombi ID? If you do not use Ombi, or can't remember, type /skip."
ACCOUNT_REGISTER_DETAIL = "How much detail do you want in your immediate notifications?\n\n_All daily and weekly content reports only contain basic information._"
ACCOUNT_REGISTER_UPGRADE = "Do you want to be notified when content you watch is upgraded?\n\nFor example, if the content is upgraded to a higher resolution, fixed, etc."
ACCOUNT_REGISTER_START = "Welcome to {}, let's get you registered so you can start using me!\n\n"+ACCOUNT_REGISTER_DETAIL
ACCOUNT_REGISTER_FAIL_REGISTERED = "_Looks like you're already registered!_\n\nUse /account to get the current status of your account."
ACCOUNT_REGISTER_FAIL_CANCELLED = "_Registration has been cancelled._\n\nUse /register to start the registration process again."

####################
# /UNWATCH COMMAND #
####################

UNWATCH_EMPTY_ARGS = "_/unwatch usage:_\n\n/unwatch <type> <name>"
UNWATCH_INCORRECT_TYPE = "_Sorry, that is not a valid type of media._"
UNWATCH_TELEVISION_SUCCESS = "_You have stopped watching_ *{}!*\n\nYou will no longer be notified for any new episodes."
UNWATCH_MOVIES_SUCCESS = "_You have stopped watching_ *{}!*\n\nYou will no longer be notified when this movie is available."
UNWATCH_TELEVISION_CALLBACK = "unwatch_SHOW_"
UNWATCH_MOVIE_CALLBACK = "unwatch_MOVIE_"

##################
# /WATCH COMMAND #
##################

WATCH_EMPTY_ARGS =  "_/watch usage:_\n\n/watch <type> <name>"
WATCH_INCORRECT_TYPE = "_Sorry, that is not a valid type of media._"
WATCH_TELEVISION_EMPTY_SEARCH = "_Sorry, no shows were found containing those words._"
WATCH_TELEVISION_FIRST_TEN = "_Here are the first ten results:_\n\nIf you cannot find the show, try making your search more specific."
WATCH_TELEVISION_FREQUENCY = "_How often do you want to be notified about new content for this show?_\n\nDaily means you won't be notified immediately, but rather in the daily update on new content for shows you watch.\n\nWeekly means you won't be notified immediately or daily, but rather in the weekly update on new content for shows you watch.\n\nIf you do not select an option, you will automatically be set to get notified immediately on the release of new content."
WATCH_TELEVISION_SUCCESS = "_You are now watching_ *{}!*\n\nYou will be notified for any new episodes for this show {}."
WATCH_MOVIES_EMPTY_SEARCH = "_Sorry, no movies were found containing those words._"
WATCH_MOVIES_FIRST_TEN = "_Here are the first ten results:_\n\nIf you cannot find the movie, try making your search more specific."
WATCH_MOVIES_SUCCESS = "_You are now watching_ *{}!*\n\nYou will be notified when this movie is available."
WATCH_TELEVISION_CALLBACK = "watch_SHOW_"
WATCH_TELEVISION_FREQ_CALLBACK = "watch_FREQ_SHOW_"
WATCH_MOVIE_CALLBACK = "watch_MOVIE_"

####################
# NOTIFIER RELATED #
####################

NOTIFIER_MEDIA_TYPE_TELEVISION = 0
NOTIFIER_MEDIA_TYPE_MOVIE = 1
NOTIFIER_MEDIA_TYPE_MUSIC = 2
NOTIFIER_FREQUENCY_IMMEDIATELY = 0
NOTIFIER_FREQUENCY_DAILY = 1
NOTIFIER_FREQUENCY_WEEKLY = 2
NOTIFIER_FREQUENCY = ["Immediately", "Daily", "Weekly"]
NOTIFIER_QUALITY_VERSIONS = ["None", "Regular Release", "PROPER Release"]
NOTIFIER_IMMEDIATELY_HEADER = "_Content Now Available:_\n\n"
NOTIFIER_DAILY_HEADER = "_Daily Content Report:_\n\n"
NOTIFIER_WEEKLY_HEADER = "_Weekly Content Report:_\n\n"
NOTIFIER_NOTHING_TO_SEND = "--- DON'T SEND ANYTHING ---"

###########
# METHODS #
###########

def minutesToSeconds(minutes):
    return minutes*MINUTE_IN_SECONDS

def hoursToSeconds(hours):
    return hours*HOUR_IN_SECONDS

def daysToSeconds(days):
    return days*DAY_IN_SECONDS

def weeksToSeconds(week):
    return week*WEEK_IN_SECONDS

def listDifference(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif

####################
# KEYBOARD MARKUPS # 
####################

for opt in range(len(DELETEACCOUNT_OPTIONS)):
    DELETEACCOUNT_OPTIONS_MARKUP.append([DELETEACCOUNT_OPTIONS[opt]])

for opt in range(len(ACCOUNT_OPTIONS)):
    ACCOUNT_OPTIONS_REPLY_MARKUP.append([ACCOUNT_OPTIONS[opt]])

for opt in range(len(ACCOUNT_STATUS)):
    ACCOUNT_STATUS_REPLY_MARKUP.append([ACCOUNT_STATUS[opt]])

for opt in range(len(ACCOUNT_DETAIL)):
    ACCOUNT_DETAIL_REPLY_MARKUP.append([ACCOUNT_DETAIL[opt]])

for opt in range(len(ACCOUNT_UPGRADE)):
    ACCOUNT_UPGRADE_REPLY_MARKUP.append([ACCOUNT_UPGRADE[opt]])