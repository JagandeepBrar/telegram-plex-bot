import telegram
import backend.api.telegram

from telegram.ext import ConversationHandler
from backend import constants, logger
from backend.api import ombi
from backend.commands import checker
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import insert, select, delete, update as update_db

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
