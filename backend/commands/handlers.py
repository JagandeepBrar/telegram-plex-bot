import backend.api.telegram as telegram
from functools import wraps
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, RegexHandler, Filters
from backend.commands.command import *
from backend import constants, logger

def initialize():
    conversationHandlers()
    commandHandlers()
    callbackQueryHandlers()
    logger.info(__name__, "Telegram command handlers initialized")

def conversationHandlers():
    telegram.dispatcher.add_handler(ConversationHandler(
        entry_points = [
            CommandHandler("start", register.register),
            CommandHandler("register", register.register)
        ],
        fallbacks = [CommandHandler("cancel", register.cancel)],
        states = {
            constants.ACCOUNT_REGISTER_STATE_DETAIL: [
                RegexHandler(constants.ACCOUNT_DETAIL_REGEX, register.detail)
            ],
            constants.ACCOUNT_REGISTER_STATE_OMBI: [
                MessageHandler(Filters.text, register.ombiRegister),
                CommandHandler("skip", register.ombiSkip)
            ],
            constants.ACCOUNT_REGISTER_STATE_UPGRADE: [
                RegexHandler(constants.ACCOUNT_UPGRADE_REGEX, register.upgrade)
            ]
        }
    ))
    telegram.dispatcher.add_handler(ConversationHandler(
        entry_points = [
            CommandHandler("account", account.account)
        ],
        fallbacks = [CommandHandler("exit", account.cancel)],
        states = {
            constants.ACCOUNT_STATE_OPTIONS: [
                RegexHandler(constants.ACCOUNT_OPTIONS_REGEX, account.options)
            ],
            constants.ACCOUNT_STATE_OMBI: [
                MessageHandler(Filters.text, account.ombiRegister),
                CommandHandler("skip", account.ombiSkip)
            ],
            constants.ACCOUNT_STATE_DETAIL: [
                RegexHandler(constants.ACCOUNT_DETAIL_REGEX, account.detail)
            ],
            constants.ACCOUNT_STATE_UPGRADE: [
                RegexHandler(constants.ACCOUNT_UPGRADE_REGEX, account.upgrade)
            ]
        }
    ))
    telegram.dispatcher.add_handler(ConversationHandler(
        entry_points = [
            CommandHandler("deleteaccount", deleteaccount.deleteaccount)
        ],
        fallbacks = [CommandHandler("cancel", deleteaccount.cancel)],
        states = {
            constants.DELETEACCOUNT_STATE_OPTIONS: [
                RegexHandler(constants.DELETEACCOUNT_OPTIONS_REGEX, deleteaccount.options)
            ]
        }
    ))

def commandHandlers():
    telegram.dispatcher.add_handler(CommandHandler("help", help.help))
    # watch related
    telegram.dispatcher.add_handler(CommandHandler("watch", watch.watch, pass_args=True))
    telegram.dispatcher.add_handler(CommandHandler("unwatch", unwatch.unwatch, pass_args=True))
    #Admin-Only
    telegram.dispatcher.add_handler(CommandHandler("access", access.access))
    telegram.dispatcher.add_handler(CommandHandler("forceupdate", forceupdate.forceupdate, pass_args=True))

def callbackQueryHandlers():
    telegram.dispatcher.add_handler(CallbackQueryHandler(access.getStatus, pattern="^"+constants.ACCESS_GETSTATUS_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(access.user, pattern="^"+constants.ACCESS_USER_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(access.setStatus, pattern="^"+constants.ACCESS_SETSTATUS_CALLBACK))

    telegram.dispatcher.add_handler(CallbackQueryHandler(watch.showSearch, pattern="^"+constants.WATCH_TELEVISION_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(watch.showFreq, pattern="^"+constants.WATCH_TELEVISION_FREQ_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(unwatch.showSearch, pattern="^"+constants.UNWATCH_TELEVISION_CALLBACK))
    
    telegram.dispatcher.add_handler(CallbackQueryHandler(watch.movieSearch, pattern="^"+constants.WATCH_MOVIE_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(unwatch.movieSearch, pattern="^"+constants.UNWATCH_MOVIE_CALLBACK))