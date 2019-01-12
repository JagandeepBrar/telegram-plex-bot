import backend.api.telegram as telegram
from functools import wraps
from telegram.ext import CommandHandler, MessageHandler
from backend.commands.command import account

def initialize():
    telegram.dispatcher.add_handler(CommandHandler("start", account.register))
