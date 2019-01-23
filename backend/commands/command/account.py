import telegram
import backend.api.telegram

from telegram.ext import ConversationHandler
from backend import constants, logger
from backend.api import ombi
from backend.commands import checker
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import insert, select, delete, update as update_db

# Start the registration process
def register(bot, update):
    if(not select.isUserRegistered(update.message.chat_id)):
        insert.insertUser(update.message.chat_id, constants.ACCOUNT_STATUS_UNVERIFIED, constants.ACCOUNT_DETAIL_SIMPLE, None, update.message.from_user.full_name)
        update.message.reply_text(constants.ACCOUNT_REGISTER_START.format(constants.BOT_NAME), parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(constants.ACCOUNT_DETAIL_REPLY_MARKUP, resize_keyboard=True))
        logger.info(__name__, "User registered - {}: {}".format(update.message.chat_id, update.message.from_user.full_name), "INFO_BLUE")
        return constants.ACCOUNT_REGISTER_STATE_DETAIL
    else:
        update.message.reply_text(constants.ACCOUNT_REGISTER_FAIL_REGISTERED, parse_mode=telegram.ParseMode.MARKDOWN)
        return ConversationHandler.END

# Register the user's detail notification preference
def registerDetail(bot, update):
    update_db.updateUserDetail(update.message.chat_id, constants.ACCOUNT_DETAIL.index(update.message.text))
    if(ombi.enabled):
        update.message.reply_text(constants.ACCOUNT_REGISTER_OMBI, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return constants.ACCOUNT_REGISTER_STATE_OMBI
    else:
        return registerFinish(bot, update)

# Register the user's ombi ID if they enter one
def registerOmbi(bot, update):
    update_db.updateUserOmbi(update.message.chat_id, update.message.text)
    return registerFinish(bot, update)

# If the user skips the Ombi ID registration
def registerOmbiSkip(bot, update):
    return registerFinish(bot, update)

# Finishes the registration process by logging and sending a message to the user
def registerFinish(bot, update):
    # Set the status
    status = constants.ACCOUNT_STATUS_UNVERIFIED
    if(backend.api.telegram.isAdmin(update.message.chat_id)):
        status = constants.ACCOUNT_STATUS_ADMIN
    elif(backend.api.telegram.auto_approve):
        status = constants.ACCOUNT_STATUS_VERIFIED
    update_db.updateUserStatus(update.message.chat_id, status)
    # Log the registration and reply with the appropriate message
    update.message.reply_text(constants.ACCOUNT_STATUS_MSG[status], parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END

# Registration cancelled: Delete the in-progress database user entry and message user on how to re-register
def registerCancel(bot, update):
    delete.deleteUser(update.message.chat_id)
    update.message.reply_text(constants.ACCOUNT_REGISTER_FAIL_CANCELLED, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END

# Check the status of the asking user, and allow them to update settings
def account(bot, update):
    if(checker.checkRegistered(update)):
        user_status = select.getUser(update.message.chat_id)[1]
        update.message.reply_text(constants.ACCOUNT_STATUS_MSG[user_status]+constants.ACCOUNT_STATUS_FOOTER_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(constants.ACCOUNT_OPTIONS_REPLY_MARKUP, resize_keyboard=True))
        return constants.ACCOUNT_STATE_OPTIONS
    else:
        return ConversationHandler.END

def accountOptions(bot, update):
    option = update.message.text
    if(option == constants.ACCOUNT_OPTIONS[0]):
        update.message.reply_text(constants.ACCOUNT_REGISTER_OMBI, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return constants.ACCOUNT_STATE_OMBI
    elif(option == constants.ACCOUNT_OPTIONS[1]):
        update.message.reply_text(constants.ACCOUNT_REGISTER_DETAIL, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(constants.ACCOUNT_DETAIL_REPLY_MARKUP, resize_keyboard=True))
        return constants.ACCOUNT_STATE_DETAIL
    else:
        return accountExit(bot, update)

def accountUpdateOmbi(bot, update):
    update_db.updateUserOmbi(update.message.chat_id, update.message.text)
    update.message.reply_text(constants.ACCOUNT_OMBI_UPDATED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return account(bot, update)

def accountUpdateOmbiSkip(bot, update):
    return account(bot, update)

def accountUpdateDetail(bot, update):
    update_db.updateUserDetail(update.message.chat_id, constants.ACCOUNT_DETAIL.index(update.message.text))
    update.message.reply_text(constants.ACCOUNT_DETAIL_UPDATED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return account(bot, update)

def accountExit(bot, update):
    user = select.getUser(update.message.chat_id)
    resp = constants.ACCOUNT_CLOSED_MSG.format(user[0], constants.ACCOUNT_STATUS[user[1]].capitalize(), constants.ACCOUNT_DETAIL[user[2]], user[3], user[4])
    update.message.reply_text(resp, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END
