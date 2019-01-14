import logging
import backend.api.telegram as telegram
from functools import wraps
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
from backend.commands.command import account, admin
from backend import constants

def initialize():
    # Account-Related
    telegram.dispatcher.add_handler(CommandHandler("start", account.register))
    telegram.dispatcher.add_handler(CommandHandler("status", account.status))
    #Admin-Only
    telegram.dispatcher.add_handler(CommandHandler("getaccess", admin.getAccess))
    telegram.dispatcher.add_handler(CommandHandler("setaccess", admin.setAccess, pass_args=True))
    telegram.dispatcher.add_handler(CommandHandler("forceupdate", admin.forceUpdate, pass_args=True))
    #CallbackQuery Handlers
    telegram.dispatcher.add_handler(CallbackQueryHandler(admin.getAccessCallback, pattern="^"+constants.ADMIN_GETACCESS_CALLBACK))

    logging.getLogger(__name__).info("Telegram command handlers initialized")
