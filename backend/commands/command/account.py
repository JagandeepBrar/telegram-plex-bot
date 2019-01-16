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
        insert.insertUser(update.message.chat_id, None, None, None, update.message.from_user.full_name)
        reply_keyboard = [['Immediately'], ['Daily'], ['Weekly']]
        update.message.reply_text(constants.ACCOUNT_REGISTER_START, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True))
        return constants.ACCOUNT_REGISTER_STATE_FREQ
    else:
        update.message.reply_text(constants.ACCOUNT_REGISTER_FAIL_REGISTERED, parse_mode=telegram.ParseMode.MARKDOWN)
        return ConversationHandler.END

# Register the user's frequency preference
def register_frequency(bot, update):
    update_db.updateUserFrequency(update.message.chat_id, constants.ACCOUNT_FREQUENCY.index(update.message.text.lower()))
    if(ombi.enabled):
        update.message.reply_text(constants.ACCOUNT_REGISTER_OMBI, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return constants.ACCOUNT_REGISTER_STATE_OMBI
    else:
        register_finish(bot, update)
        return ConversationHandler.END

# Register the user's ombi ID if they enter one
def register_ombi(bot, update):
    update_db.updateUserOmbi(update.message.chat_id, update.message.text)
    register_finish(bot, update)
    return ConversationHandler.END

# If the user skips the Ombi ID registration
def register_ombi_skip(bot, update):
    register_finish(bot, update)
    return ConversationHandler.END

# Finishes the registration process by logging and sending a message to the user
def register_finish(bot, update):
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

# Registration cancelled: Delete the in-progress database user entry and message user on how to re-register
def register_cancel(bot, update):
    delete.deleteUser(update.message.chat_id)
    update.message.reply_text(constants.ACCOUNT_REGISTER_FAIL_CANCELLED, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END

# Check the status of the asking user, and allow them to add their ombi ID
@send_typing_action
def account(bot, update):
    if(checker.checkRegistered(update)):
        user_status = select.getUser(update.message.chat_id)[1]
        update.message.reply_text(constants.ACCOUNT_STATUS_MSG[user_status], parse_mode=telegram.ParseMode.MARKDOWN)