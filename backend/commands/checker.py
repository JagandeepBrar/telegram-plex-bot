import telegram
from backend import constants
from backend.database.statement import select

# Checks if the supplied update is from a registered user
def checkRegistered(update):
    if(not select.isUserRegistered(update.message.chat_id)):
        update.message.reply_text(constants.CHECKER_UNREGISTERED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return False
    return True

# Checks if the supplied update is from an admin user
def checkAdmin(update):
    if(not select.isUserStatus(update.message.chat_id, constants.ACCOUNT_STATUS_ADMIN)):
        update.message.reply_text(constants.CHECKER_UNAUTHORIZED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return False
    return True

# Checks if the supplied update is from an unverified user
def checkUnverified(update):
    if(select.isUserStatus(update.message.chat_id, constants.ACCOUNT_STATUS_UNVERIFIED)):
        update.message.reply_text(constants.CHECKER_UNVERIFIED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return True
    return False

# Checks if the supplied update is from a banned user
def checkBanned(update):
    if(select.isUserStatus(update.message.chat_id, constants.ACCOUNT_STATUS_BANNED)):
        update.message.reply_text(constants.CHECKER_BANNED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return True
    return False

# Check if the supplied update is from a restricted user
def checkRestricted(update, command):
    if(select.isUserStatus(update.message.chat_id, constants.ACCOUNT_STATUS_RESTRICTED)):
            update.message.reply_text(constants.CHECKER_RESTRICTED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
            return True
    return False

# Runs all checks to see if the command can be executed
def checkAllowed(update, command):
    if(
        not checkRegistered(update) or 
        checkUnverified(update) or
        checkBanned(update) or
        checkRestricted(update, command)
    ):
        return False
    return True

# Runs all checks to see if the command can be executed for admins
def checkAdminAllowed(update):
    if(
        not checkRegistered(update) or
        not checkAdmin(update)
    ):
        return False
    return True
