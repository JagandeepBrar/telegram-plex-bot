import telegram
import logging
import backend.api.telegram

from backend import constants
from backend.scheduler.jobs import catalogue
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import insert, select, update as update_db
from backend.commands.command import television, movies
from backend.commands import checker

# [ADMIN ONLY] Gets a list of users with access status (selected through inline keyboard)
@send_typing_action
def getAccess(bot, update):
    if(checker.checkAdminAllowed(update)):
        keyboard = []
        for status in range(0, len(constants.ACCOUNT_STATUS)):
            keyboard.append([telegram.InlineKeyboardButton(constants.ACCOUNT_STATUS[status].capitalize(), callback_data=constants.ADMIN_GETACCESS_CALLBACK+constants.ACCOUNT_STATUS[status])])
        reply_markup = telegram.InlineKeyboardMarkup(keyboard)
        update.message.reply_text(constants.ADMIN_GETACCESS_MSG, reply_markup=reply_markup, parse_mode=telegram.ParseMode.MARKDOWN)

# [ADMIN ONLY] CallbackQueryHandler for getAccess()
def getAccessCallback(bot, update):
    status = constants.ACCOUNT_STATUS.index(update.callback_query.data[len(constants.ADMIN_GETACCESS_CALLBACK):])
    users = select.getUsersWithStatus(status)
    resp = constants.ADMIN_GETACCESS_HEADER.format(constants.ACCOUNT_STATUS[status].capitalize())
    for user in users:
        resp += constants.ADMIN_GETACCESS_RESP.format(user[0], user[5])
    bot.edit_message_text(text=resp,chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, parse_mode=telegram.ParseMode.MARKDOWN)

# [ADMIN ONLY] Set the user access status for a user
@send_typing_action
def setAccess(bot, update, args):
    if(checker.checkAdminAllowed(update)):
        resp = constants.ADMIN_SETACCESS_FAIL_ARGS
        if(len(args) == 2):
            if(args[0].isdigit()):
                try:
                    status = constants.ACCOUNT_STATUS.index(args[1].lower())
                    user = select.getUser(args[0])
                    if(user is not None):
                        update_db.updateUserStatus(user[0], status)
                        user = select.getUser(args[0])
                        resp = constants.ADMIN_SETACCESS_SUCCESS.format(user[0], constants.ACCOUNT_STATUS[status].capitalize(), constants.ACCOUNT_FREQUENCY[int(user[2])].capitalize(), constants.ACCOUNT_DETAIL[user[3]], user[4], user[5])
                        bot.send_message(chat_id=user[0], text=constants.ACCOUNT_STATUS_MSG[status], parse_mode=telegram.ParseMode.MARKDOWN)
                        logging.getLogger(__name__).info("{}: {} access status has been updated to {}".format(user[0], user[5], constants.ACCOUNT_STATUS[status]))
                    else:
                        resp = constants.ADMIN_SETACCESS_FAIL_TID
                except:
                    resp = constants.ADMIN_SETACCESS_FAIL_STATUS
        elif(len(args) == 1):
            if(args[0] == "verifyall"):
                users = select.getUsersWithStatus(constants.ACCOUNT_STATUS_UNVERIFIED)
                if(len(users) != 0):
                    for user in users:
                        update_db.updateUserStatus(user[0], constants.ACCOUNT_STATUS_VERIFIED)
                        bot.send_message(chat_id=user[0], text=constants.ACCOUNT_STATUS_VERIFIED_MSG, parse_mode=telegram.ParseMode.MARKDOWN)
                        logging.getLogger(__name__).info("{}: {} access status has been updated to {}".format(user[0], user[4], constants.ACCOUNT_STATUS[constants.ACCOUNT_STATUS_VERIFIED]))
                    resp = constants.ADMIN_SETACCESS_SUCCESS_VERIFYALL
                else:
                    resp = constants.ADMIN_SETACCESS_FAIL_VERIFYALL
        update.message.reply_text(resp, parse_mode=telegram.ParseMode.MARKDOWN)

# [ADMIN ONLY] Force update the database(s)
@send_typing_action
def forceUpdate(bot, update, args):
    if(checker.checkAdminAllowed(update)):
        if(len(args) == 1):
            if(args[0] == "shows"):
                television.forceUpdate(bot, update)
            elif(args[0] == "movies"):
                movies.forceUpdate(bot, update)
            elif(args[0] == "all"):
                television.forceUpdate(bot, update)
                movies.forceUpdate(bot, update)
            else:
                update.message.reply_text(constants.ADMIN_FORCEUPDATE_FAILED_TYPE, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            update.message.reply_text(constants.ADMIN_FORCEUPDATE_FAILED_ARGS, parse_mode=telegram.ParseMode.MARKDOWN)