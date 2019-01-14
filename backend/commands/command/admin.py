import telegram
import logging
import backend.api.telegram

from backend import constants
from backend.scheduler.jobs import catalogue
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import insert, select, update as update_db
from backend.commands.command import television, movies

# [ADMIN ONLY] Gets a list of users with access status (selected through inline keyboard)
@send_typing_action
def getAccess(bot, update):
    if(update.message.chat_id in select.getAdmins()):
        keyboard = []
        for status in range(0, len(constants.ACCOUNT_STATUS)):
            keyboard.append([telegram.InlineKeyboardButton(constants.ACCOUNT_STATUS[status].capitalize(), callback_data=constants.ADMIN_GETACCESS_CALLBACK+constants.ACCOUNT_STATUS[status])])
        reply_markup = telegram.InlineKeyboardMarkup(keyboard)
        update.message.reply_text(constants.ADMIN_GETACCESS_MSG, reply_markup=reply_markup)
    else:
        bot.send_message(chat_id=update.message.chat_id, text=constants.ACCOUNT_UNAUTHORIZED, parse_mode=telegram.ParseMode.MARKDOWN)

# [ADMIN ONLY] CallbackQueryHandler for getAccess()
def getAccessCallback(bot, update):
    status = constants.ACCOUNT_STATUS.index(update.callback_query.data[len(constants.ADMIN_GETACCESS_CALLBACK):])
    users = select.getUsersWithStatus(status)
    resp = constants.ADMIN_GETACCESS_HEADER.format(constants.ACCOUNT_STATUS[status].capitalize())
    for user in users:
        resp += constants.ADMIN_GETACCESS_RESP.format(user[0], user[3])
    bot.edit_message_text(text=resp,chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, parse_mode=telegram.ParseMode.MARKDOWN)

# [ADMIN ONLY] Set the user access status for a user
@send_typing_action
def setAccess(bot, update, args):
    if(update.message.chat_id in select.getAdmins()):
        resp = constants.ADMIN_SETACCESS_FAIL_ARGS
        if(len(args) == 2):
            if(args[0].isdigit()):
                try:
                    status = constants.ACCOUNT_STATUS.index(args[1].lower())
                    user = select.getUser(args[0])
                    if(user is not None):
                        update_db.updateUser(user[0], user[1], status, user[3])
                        user = select.getUser(args[0])
                        resp = constants.ADMIN_SETACCESS_SUCCESS.format(user[0], user[1], constants.ACCOUNT_STATUS[status].capitalize(), user[3])
                        logging.getLogger(__name__).info("{}: {} access status has been updated to {}".format(user[0], user[3], constants.ACCOUNT_STATUS[status]))
                    else:
                        resp = constants.ADMIN_SETACCESS_FAIL_TID
                except:
                    resp = constants.ADMIN_SETACCESS_FAIL_STATUS
        elif(len(args) == 1):
            if(args[0] == "verifyall"):
                users = select.getUsersWithStatus(constants.ACCOUNT_STATUS_UNVERIFIED)
                if(len(users) != 0):
                    for user in users:
                        update_db.updateUser(user[0], user[1], constants.ACCOUNT_STATUS_VERIFIED, user[3])
                        logging.getLogger(__name__).info("{}: {} access status has been updated to {}".format(user[0], user[3], constants.ACCOUNT_STATUS[constants.ACCOUNT_STATUS_VERIFIED]))
                    resp = constants.ADMIN_SETACCESS_SUCCESS_VERIFYALL
                else:
                    resp = constants.ADMIN_SETACCESS_FAIL_VERIFYALL
        bot.send_message(chat_id=update.message.chat_id, text=resp, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.send_message(chat_id=update.message.chat_id, text=constants.ACCOUNT_UNAUTHORIZED, parse_mode=telegram.ParseMode.MARKDOWN)

# [ADMIN ONLY] Force update the database(s)
@send_typing_action
def forceUpdate(bot, update, args):
    if(update.message.chat_id in select.getAdmins()):
        if(len(args) == 1):
            if(args[0] == "shows"):
                television.forceUpdate(bot, update)
            elif(args[0] == "movies"):
                movies.forceUpdate(bot, update)
            elif(args[0] == "all"):
                television.forceUpdate(bot, update)
                movies.forceUpdate(bot, update)
            else:
                bot.send_message(chat_id=update.message.chat_id, text=constants.ADMIN_FORCEUPDATE_FAILED_TYPE, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            bot.send_message(chat_id=update.message.chat_id, text=constants.ADMIN_FORCEUPDATE_FAILED_ARGS, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.send_message(chat_id=update.message.chat_id, text=constants.ACCOUNT_UNAUTHORIZED, parse_mode=telegram.ParseMode.MARKDOWN)
