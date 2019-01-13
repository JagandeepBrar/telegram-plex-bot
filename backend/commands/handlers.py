import backend.api.telegram as telegram
from functools import wraps
from telegram.ext import CommandHandler, MessageHandler
from backend.commands.command import account

def initialize():
    # Account-Related
    telegram.dispatcher.add_handler(CommandHandler("start", account.register))
    telegram.dispatcher.add_handler(CommandHandler("check", account.check))
    telegram.dispatcher.add_handler(CommandHandler("setstatus", account.set_status))