import datetime

###########
# GENERAL #
###########

HOUR_IN_SECONDS = 3600
DAY_IN_SECONDS = HOUR_IN_SECONDS*24
WEEK_IN_SECONDS = DAY_IN_SECONDS*7
INSERT_DATE = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)


#################################
# CONFIGURATION & API ENDPOINTS #
#################################

CONFIG_FILE = "config.ini"
DB_FILE = "database.db"
BOT_NAME = "Plex Assistant"

SONARR_SYSTEM_STATUS = "system/status"
SONARR_SERIES = "/series"
SONARR_SERIES_LOOKUP = "/series/lookup?term=tvdb:"

RADARR_SYSTEM_STATUS = "system/status"
RADARR_MOVIES = "/movie"
RADARR_MOVIES_LOOKUP = "/movie/lookup/tmdb?tmdbId="

############################
# ACCOUNT COMMANDS RELATED #
############################

# ACCOUNT COMMAND MESSAGES
ACCOUNT_UNAUTHORIZED = "_Sorry, this command can only be run by admins/owners._"

# USER FREQUENCY LEVELS

ACCOUNT_FREQUENCY_IMMEDIATE = 0
ACCOUNT_FREQUENCY_DAILY = 1
ACCOUNT_FREQUENCY_MONTHLY = 2
ACCOUNT_FREQUENCY = ["immediate", "daily", "monthly"]

# USER ACCESS LEVELS
ACCOUNT_STATUS_ADMIN = 0
ACCOUNT_STATUS_UNVERIFIED = 1
ACCOUNT_STATUS_VERIFIED = 2
ACCOUNT_STATUS_RESTRICTED = 3
ACCOUNT_STATUS_BANNED = 4
ACCOUNT_STATUS = ["admin", "unverified", "verified", "restricted", "banned"]

# USER STATUS MESSAGES
ACCOUNT_STATUS_ADMIN_MSG = "*You are registered as an admin/owner!*\n\nYou have full access to all commands, type /help to see all available commands."
ACCOUNT_STATUS_PENDING_MSG = "*You are registered!*\n\nYour account is pending verification, you will be notified when verification is complete."
ACCOUNT_STATUS_VERIFIED_MSG = "*You are registered and verified!*\n\nType /help to see all available commands."
ACCOUNT_STATUS_RESTRICTED_MSG = "*You are registered and verified!*\n\nYour account is active, but restricted. Please inquire with the admin(s)."
ACCOUNT_STATUS_BANNED_MSG = "*You are banned!*\n\nPlease inquire with the admins(s)."
ACCOUNT_STATUS_MSG = [ACCOUNT_STATUS_ADMIN_MSG, ACCOUNT_STATUS_PENDING_MSG, ACCOUNT_STATUS_VERIFIED_MSG, ACCOUNT_STATUS_RESTRICTED_MSG, ACCOUNT_STATUS_BANNED_MSG]

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