import logging
import backend.api.telegram as telegram
from functools import wraps
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
from backend.commands.command import account
from backend import constants

def initialize():
    # Account-Related
    telegram.dispatcher.add_handler(CommandHandler("start", account.register))
    telegram.dispatcher.add_handler(CommandHandler("check", account.check))
    telegram.dispatcher.add_handler(CommandHandler("getaccess", account.getAccess))
    telegram.dispatcher.add_handler(CommandHandler("setaccess", account.setAccess, pass_args=True))
    telegram.dispatcher.add_handler(CallbackQueryHandler(account.getAccessCallback, pattern="^"+constants.ACCOUNT_GETACCESS_CALLBACK))
    logging.getLogger(__name__).info("Telegram command handlers initialized")