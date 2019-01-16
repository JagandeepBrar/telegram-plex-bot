import telegram
import logging
import backend.api.telegram

from telegram.ext import ConversationHandler
from backend import constants
from backend.api import ombi
from backend.commands import checker
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import insert, select, delete, update as update_db

# Start the registration process
def register(bot, update):
    if(not select.isUserRegistered(update.message.chat_id)):
        insert.insertUser(update.message.chat_id, None, None, None, None, update.message.from_user.full_name)
        reply_keyboard = [[constants.ACCOUNT_FREQUENCY[0]], [constants.ACCOUNT_FREQUENCY[1]], [constants.ACCOUNT_FREQUENCY[2]]]
        update.message.reply_text(constants.ACCOUNT_REGISTER_START, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
        return constants.ACCOUNT_REGISTER_STATE_FREQ
    else:
        update.message.reply_text(constants.ACCOUNT_REGISTER_FAIL_REGISTERED, parse_mode=telegram.ParseMode.MARKDOWN)
        return ConversationHandler.END

# Register the user's frequency preference
def registerFrequency(bot, update):
    update_db.updateUserFrequency(update.message.chat_id, constants.ACCOUNT_FREQUENCY.index(update.message.text))
    reply_keyboard = [[constants.ACCOUNT_DETAIL[0]], [constants.ACCOUNT_DETAIL[1]]]
    update.message.reply_text(constants.ACCOUNT_REGISTER_DETAIL, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
    return constants.ACCOUNT_REGISTER_STATE_DETAIL

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
    logging.getLogger(__name__).info("User registered - {}: {}".format(update.message.chat_id, update.message.from_user.full_name))
    update.message.reply_text(constants.ACCOUNT_STATUS_MSG[status], parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END

# Registration cancelled: Delete the in-progress database user entry and message user on how to re-register
def registerCancel(bot, update):
    delete.deleteUser(update.message.chat_id)
    update.message.reply_text(constants.ACCOUNT_REGISTER_FAIL_CANCELLED, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END

# Check the status of the asking user, and allow them to add their ombi ID or update frequency
def account(bot, update):
    if(checker.checkRegistered(update)):
        user_status = select.getUser(update.message.chat_id)[1]
        reply_keyboard = [[constants.ACCOUNT_OMBI], [constants.ACCOUNT_FREQ], [constants.ACCOUNT_DEET], [constants.ACCOUNT_EXIT]]
        update.message.reply_text(constants.ACCOUNT_STATUS_MSG[user_status]+constants.ACCOUNT_STATUS_FOOTER_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
        return constants.ACCOUNT_STATE_OPTIONS
    else:
        return ConversationHandler.END

def accountOptions(bot, update):
    option = update.message.text
    if(option == constants.ACCOUNT_FREQ):
        reply_keyboard = [[constants.ACCOUNT_FREQUENCY[0]], [constants.ACCOUNT_FREQUENCY[1]], [constants.ACCOUNT_FREQUENCY[2]]]
        update.message.reply_text(constants.ACCOUNT_REGISTER_FREQ, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
        return constants.ACCOUNT_STATE_FREQ
    elif(option == constants.ACCOUNT_OMBI):
        update.message.reply_text(constants.ACCOUNT_REGISTER_OMBI, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return constants.ACCOUNT_STATE_OMBI
    elif(option == constants.ACCOUNT_DEET):
        reply_keyboard = [[constants.ACCOUNT_DETAIL[0]], [constants.ACCOUNT_DETAIL[1]]]
        update.message.reply_text(constants.ACCOUNT_REGISTER_DETAIL, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
        return constants.ACCOUNT_STATE_DETAIL
    else:
        return accountExit(bot, update)

def accountUpdateOmbi(bot, update):
    update_db.updateUserOmbi(update.message.chat_id, update.message.text)
    update.message.reply_text(constants.ACCOUNT_OMBI_UPDATED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return account(bot, update)

def accountUpdateOmbiSkip(bot, update):
    return account(bot, update)

def accountUpdateFrequency(bot, update):
    update_db.updateUserFrequency(update.message.chat_id, constants.ACCOUNT_FREQUENCY.index(update.message.text))
    update.message.reply_text(constants.ACCOUNT_FREQ_UPDATED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return account(bot, update)

def accountUpdateDetail(bot, update):
    update_db.updateUserDetail(update.message.chat_id, constants.ACCOUNT_DETAIL.index(update.message.text))
    update.message.reply_text(constants.ACCOUNT_DETAIL_UPDATED_MSG, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return account(bot, update)

def accountExit(bot, update):
    user = select.getUser(update.message.chat_id)
    resp = constants.ACCOUNT_CLOSED_MSG.format(user[0], constants.ACCOUNT_STATUS[user[1]].capitalize(), constants.ACCOUNT_FREQUENCY[user[2]], constants.ACCOUNT_DETAIL[user[3]], user[4], user[5])
    update.message.reply_text(resp, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END
