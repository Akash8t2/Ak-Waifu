from telegram import Update
from telegram.ext import CallbackContext
from chatbot import get_chatbot_reply
from memory import update_memory
from config import WAFU_NAME

def chat_handler(update: Update, context: CallbackContext):
    msg = update.message.text.lower()
    user_id = update.effective_user.id
    if WAFU_NAME in msg:
        update_memory(user_id, msg)
        reply = get_chatbot_reply(msg, user_id)
        update.message.reply_text(reply)