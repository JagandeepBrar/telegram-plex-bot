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

RESTRICTED_NOTIFYSHOW = True
RESTRICTED_NOTIFYMOVIE = True

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
INSERT_DATE = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)

############################
# ACCOUNT COMMANDS RELATED #
############################

# ACCOUNT COMMAND OPTIONS

ACCOUNT_STATE_OPTIONS, ACCOUNT_STATE_OMBI, ACCOUNT_STATE_FREQ = range(3)
ACCOUNT_OMBI = "Update Ombi ID"
ACCOUNT_FREQ = "Update Notification Frequency"
ACCOUNT_EXIT = "Exit"
ACCOUNT_OPTIONS_REGEX = "^(Update Ombi ID|Update Notification Frequency|Exit)$"

ACCOUNT_FREQ_UPDATED_MSG = "_Notification frequency has been updated._"
ACCOUNT_OMBI_UPDATED_MSG = "_Ombi ID has been updated._"
ACCOUNT_CLOSED_MSG = "_Account settings have been saved. Updated user information:_\n\n*Telegram ID:* {}\n*Status:* {}\n*Frequency:* {}\n*Ombi ID:* {}\n*Name:* {}\n"

# ACCOUNT STATUS INCORRECT MESSAGES

ACCOUNT_UNAUTHORIZED = "_Sorry, this command can only be run by admins/owners._"
ACCOUNT_UNREGISTERED = "_Sorry, you are not registered._\n\nUse /register to get started!"
ACCOUNT_UNVERIFIED = "_Sorry, you are unverified._\n\nPlease wait for an admin/owner to verify your account."
ACCOUNT_RESTRICTED = "_Sorry, you are restricted._\n\nThis command can only be run by unrestricted accounts."
ACCOUNT_BANNED = "_Sorry, you are banned._\n\nThis command can only be run by unbanned accounts."

# ACCOUNT REGISTRATION 

ACCOUNT_REGISTER_STATE_FREQ, ACCOUNT_REGISTER_STATE_OMBI = range(2)
ACCOUNT_REGISTER_FREQ = "How frequently do you want to be notified on your monitored shows and movies?"
ACCOUNT_REGISTER_OMBI = "What is your Ombi ID? If you do not use Ombi, or can't remember, type /skip."
ACCOUNT_REGISTER_START = "Welcome to {}, let's get you registered so you can start using me!\n\n".format(BOT_NAME)+ACCOUNT_REGISTER_FREQ
ACCOUNT_REGISTER_FAIL_REGISTERED = "_Looks like you're already registered!_\n\nUse /account to get the current status of your account."
ACCOUNT_REGISTER_FAIL_CANCELLED = "_Registration has been cancelled._\n\nUse /register to start the registration process again."

# USER FREQUENCY LEVELS

ACCOUNT_FREQUENCY_IMMEDIATELY = 0
ACCOUNT_FREQUENCY_DAILY = 1
ACCOUNT_FREQUENCY_WEEKLY = 2
ACCOUNT_FREQUENCY = ["Immediately", "Daily", "Weekly"]
ACCOUNT_FREQUENCY_REGEX = "^(Immediately|Daily|Weekly)$"

# USER ACCESS LEVELS
ACCOUNT_STATUS_ADMIN = 0
ACCOUNT_STATUS_UNVERIFIED = 1
ACCOUNT_STATUS_VERIFIED = 2
ACCOUNT_STATUS_RESTRICTED = 3
ACCOUNT_STATUS_BANNED = 4
ACCOUNT_STATUS = ["admin", "unverified", "verified", "restricted", "banned"]

# USER STATUS MESSAGES
ACCOUNT_STATUS_ADMIN_MSG = "*You are registered as an admin/owner!*\n\nYou have full access to all commands, use /help to see all available commands."
ACCOUNT_STATUS_PENDING_MSG = "*You are registered!*\n\nYour account is pending verification, you will be notified when verification is complete."
ACCOUNT_STATUS_VERIFIED_MSG = "*You are registered and verified!*\n\nUse /help to see all available commands."
ACCOUNT_STATUS_RESTRICTED_MSG = "*You are verifed but restricted!*\n\nYour account is active, but your access is restricted. Please inquire with the admin(s)."
ACCOUNT_STATUS_BANNED_MSG = "*You are banned!*\n\nPlease inquire with the admins(s)."
ACCOUNT_STATUS_MSG = [ACCOUNT_STATUS_ADMIN_MSG, ACCOUNT_STATUS_PENDING_MSG, ACCOUNT_STATUS_VERIFIED_MSG, ACCOUNT_STATUS_RESTRICTED_MSG, ACCOUNT_STATUS_BANNED_MSG]

ACCOUNT_STATUS_FOOTER_MSG = "\n\nTap \"Exit\" or type /exit to exit account settings."

###############################
# TELEVISION COMMANDS RELATED #
###############################

TELEVISION_FORCEUPDATE = "_Television database has been updated._"

###########################
# MOVIES COMMANDS RELATED #
###########################

MOVIES_FORCEUPDATE = "_Movies database has been updated._"

##########################
# ADMIN COMMANDS RELATED #
##########################

ADMIN_GETACCESS_MSG ="Please select the user access level:"
ADMIN_GETACCESS_HEADER = "_{} User(s)_:\n\n"
ADMIN_GETACCESS_RESP = "`{}` - {}\n"

ADMIN_SETACCESS_SUCCESS = "_Successfully updated the user status. Updated user information:_\n\n*Telegram ID:* {}\n*Status:* {}\n*Frequency:* {}\n*Ombi ID:* {}\n*Name:* {}\n"
ADMIN_SETACCESS_SUCCESS_VERIFYALL = "_Successfully updated all unverified users to verified users._"
ADMIN_SETACCESS_FAIL_ARGS = "_/setaccess usage:_\n\n/setaccess <Telegram ID (Integer)> <Status (String)>\n\n_To verify all unverified users:_\n\n/setaccess verifyall"
ADMIN_SETACCESS_FAIL_TID = "_The supplied Telegram ID is not in the database of users._\n\nUse /getaccess to find a user's ID."
ADMIN_SETACCESS_FAIL_STATUS = "_The supplied status is not a valid status. Valid statuses include:_\n\n- `admin`\n- `unverified`\n- `verified`\n- `restricted`\n- `banned`"
ADMIN_SETACCESS_FAIL_VERIFYALL = "_There are no unverified users._"

ADMIN_FORCEUPDATE_FAILED_ARGS = "_/forceupdate usage:_\n\n/forceupdate <Database (String)>"
ADMIN_FORCEUPDATE_FAILED_TYPE = "_The supplied database is not a valid database. Valid databases include:_\n\n- `shows`\n- `movies`\n- `all`"

####################
# HANDLER PREFIXES #
####################

ADMIN_GETACCESS_CALLBACK = "account_GETACCESS_"

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