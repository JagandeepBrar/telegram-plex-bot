import telegram

from telegram.ext import ConversationHandler
from backend import constants
from backend.database.statement import select, delete
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.commands import checker

def deleteaccount(bot, update):
    if(checker.checkRegistered(update)):
        status = select.getUser(update.message.chat_id)[1]
        if(int(status) == constants.ACCOUNT_STATUS_BANNED or int(status) == constants.ACCOUNT_STATUS_RESTRICTED):
            update.message.reply_text(constants.DELETEACCOUNT_UNAUTHORIZED, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            update.message.reply_text(constants.DELETEACCOUNT_CONFIRM, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardMarkup(constants.DELETEACCOUNT_OPTIONS_MARKUP, resize_keyboard=True))
            return constants.DELETEACCOUNT_STATE_OPTIONS
    return ConversationHandler.END

def cancel(bot, update):
    update.message.reply_text(constants.DELETEACCOUNT_CANCEL, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END

def options(bot, update):
    option = update.message.text
    if(option == constants.DELETEACCOUNT_OPTIONS[0]):
        return confirm(bot, update)
    else:
        return cancel(bot, update)

def confirm(bot, update):
    delete.deleteUser(update.message.chat_id)
    update.message.reply_text(constants.DELETEACCOUNT_SUCCESS, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END