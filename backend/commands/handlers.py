import logging
import backend.api.telegram as telegram
from functools import wraps
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, RegexHandler, Filters
from backend.commands.command import account, admin, movies, television, watcher
from backend import constants

def initialize():
    conversationHandlers()
    commandHandlers()
    callbackQueryHandlers()
    logging.getLogger(__name__).info("Telegram command handlers initialized")

def conversationHandlers():
    telegram.dispatcher.add_handler(ConversationHandler(
        entry_points = [
            CommandHandler("start", account.register),
            CommandHandler("register", account.register)
        ],
        fallbacks = [CommandHandler("cancel", account.registerCancel)],
        states = {
            constants.ACCOUNT_REGISTER_STATE_FREQ: [
                RegexHandler(constants.ACCOUNT_FREQUENCY_REGEX, account.registerFrequency)
            ],
            constants.ACCOUNT_REGISTER_STATE_DETAIL: [
                RegexHandler(constants.ACCOUNT_DETAIL_REGEX, account.registerDetail)
            ],
            constants.ACCOUNT_REGISTER_STATE_OMBI: [
                MessageHandler(Filters.text, account.registerOmbi),
                CommandHandler("skip", account.registerOmbiSkip)
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
            ],
            constants.ACCOUNT_STATE_FREQ: [
                RegexHandler(constants.ACCOUNT_FREQUENCY_REGEX, account.accountUpdateFrequency)
            ]
        }
    ))

def commandHandlers():
    # Watcher related
    telegram.dispatcher.add_handler(CommandHandler("watch", watcher.watch, pass_args=True))
    telegram.dispatcher.add_handler(CommandHandler("unwatch", watcher.watch, pass_args=True))
    #Admin-Only
    telegram.dispatcher.add_handler(CommandHandler("access", admin.access))
    telegram.dispatcher.add_handler(CommandHandler("forceupdate", admin.forceUpdate, pass_args=True))

def callbackQueryHandlers():
    telegram.dispatcher.add_handler(CallbackQueryHandler(admin.accessTypeCallback, pattern="^"+constants.ADMIN_ACCESS_TYPE_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(admin.accessUserCallback, pattern="^"+constants.ADMIN_ACCESS_USER_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(admin.accessSetCallback, pattern="^"+constants.ADMIN_ACCESS_SET_CALLBACK))

    telegram.dispatcher.add_handler(CallbackQueryHandler(television.watchShowCallback, pattern="^"+constants.TELEVISION_WATCH_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(television.unwatchShowCallback, pattern="^"+constants.TELEVISION_UNWATCH_CALLBACK))
    
    telegram.dispatcher.add_handler(CallbackQueryHandler(movies.watchMovieCallback, pattern="^"+constants.MOVIES_WATCH_CALLBACK))
    telegram.dispatcher.add_handler(CallbackQueryHandler(movies.unwatchMovieCallback, pattern="^"+constants.MOVIES_UNWATCH_CALLBACK))