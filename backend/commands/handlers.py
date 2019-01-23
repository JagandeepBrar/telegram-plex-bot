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
        fallbacks = [CommandHandler("cancel", register.registerCancel)],
        states = {
            constants.ACCOUNT_REGISTER_STATE_DETAIL: [
                RegexHandler(constants.ACCOUNT_DETAIL_REGEX, register.registerDetail)
            ],
            constants.ACCOUNT_REGISTER_STATE_OMBI: [
                MessageHandler(Filters.text, register.registerOmbi),
                CommandHandler("skip", register.registerOmbiSkip)
            ]
        }
    ))
    telegram.dispatcher.add_handler(ConversationHandler(
        entry_points = [
            CommandHandler("account", account.account)
        ],
        fallbacks = [CommandHandler("exit", account.accountExit)],
        states = {
            constants.ACCOUNT_STATE_OPTIONS: [
                RegexHandler(constants.ACCOUNT_OPTIONS_REGEX, account.accountOptions)
            ],
            constants.ACCOUNT_STATE_OMBI: [
                MessageHandler(Filters.text, account.accountUpdateOmbi),
                CommandHandler("skip", account.accountUpdateOmbiSkip)
            ],
            constants.ACCOUNT_STATE_DETAIL: [
                RegexHandler(constants.ACCOUNT_DETAIL_REGEX, account.accountUpdateDetail)
            ]
        }
    ))

def commandHandlers():
    # watch related
    telegram.dispatcher.add_handler(CommandHandler("watch", watch.watch, pass_args=True))
    telegram.dispatcher.add_handler(CommandHandler("unwatch", unwatch.unwatch, pass_args=True))
    #Admin-Only
    telegram.dispatcher.add_handler(CommandHandler("access", access.access))
    telegram.dispatcher.add_handler(CommandHandler("forceupdate", forceupdate.forceupdate, pass_args=True))

def callbackQueryHandlers():
    telegram.dispatcher.add_handler(CallbackQueryHandler(access.accessTypeCallback, pattern="^"+constants.ADMIN_ACCESS_TYPE_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(access.accessUserCallback, pattern="^"+constants.ADMIN_ACCESS_USER_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(access.accessSetCallback, pattern="^"+constants.ADMIN_ACCESS_SET_CALLBACK))

    telegram.dispatcher.add_handler(CallbackQueryHandler(watch.watchShowCallback, pattern="^"+constants.TELEVISION_WATCH_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(watch.watchShowFreqCallback, pattern="^"+constants.TELEVISION_WATCH_FREQ_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(unwatch.unwatchShowCallback, pattern="^"+constants.TELEVISION_UNWATCH_CALLBACK))
    
    telegram.dispatcher.add_handler(CallbackQueryHandler(watch.watchMovieCallback, pattern="^"+constants.MOVIES_WATCH_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(unwatch.unwatchMovieCallback, pattern="^"+constants.MOVIES_UNWATCH_CALLBACK))