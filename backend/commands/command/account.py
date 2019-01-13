import telegram
import backend.commands.messages as messages
from backend.commands.wrapper import send_typing_action, send_upload_photo_action, send_upload_video_action
from backend.database.statement import insert

# Register the user (add to 'users' table in database)
@send_typing_action
def register(bot, update):
    insert.insertUser(update.message.chat_id, update.message.from_user.full_name)
    bot.send_message(chat_id=update.message.chat_id, text=messages.REGISTER_PENDING, parse_mode=telegram.ParseMode.MARKDOWN)

