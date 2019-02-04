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
        insert.insertUser(update.message.chat_id, constants.ACCOUNT_STATUS_UNVERIFIED, constants.ACCOUNT_DETAIL_SIMPLE, constants.ACCOUNT_UPGRADE_NO, None, update.message.from_user.full_name)
        update.message.reply_text(constants.ACCOUNT_REGISTER_START.format(constants.BOT_NAME), parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(constants.ACCOUNT_DETAIL_REPLY_MARKUP, resize_keyboard=True))
        logger.info(__name__, "User registered - {}: {}".format(update.message.chat_id, update.message.from_user.full_name), "INFO_BLUE")
        return constants.ACCOUNT_REGISTER_STATE_DETAIL
    else:
        update.message.reply_text(constants.ACCOUNT_REGISTER_FAIL_REGISTERED, parse_mode=telegram.ParseMode.MARKDOWN)
        return ConversationHandler.END

# Register the user's detail notification preference
def detail(bot, update):
    update_db.updateUserDetail(update.message.chat_id, constants.ACCOUNT_DETAIL.index(update.message.text))
    update.message.reply_text(constants.ACCOUNT_REGISTER_UPGRADE, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(constants.ACCOUNT_UPGRADE_REPLY_MARKUP, resize_keyboard=True))
    return constants.ACCOUNT_REGISTER_STATE_UPGRADE

# Register the user's ombi ID if they enter one
def ombiRegister(bot, update):
    update_db.updateUserOmbi(update.message.chat_id, update.message.text)
    return finish(bot, update)

# If the user skips the Ombi ID registration
def ombiSkip(bot, update):
    return finish(bot, update)

# Register the user's upgraded content preference
def upgrade(bot, update):
    update_db.updateUserUpgrade(update.message.chat_id, update.message.text)
    if(ombi.enabled):
        update.message.reply_text(constants.ACCOUNT_REGISTER_OMBI, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
        return constants.ACCOUNT_REGISTER_STATE_OMBI
    else:
        return finish(bot, update)

# Finishes the registration process by logging and sending a message to the user
def finish(bot, update):
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
def cancel(bot, update):
    delete.deleteUser(update.message.chat_id)
    update.message.reply_text(constants.ACCOUNT_REGISTER_FAIL_CANCELLED, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END
