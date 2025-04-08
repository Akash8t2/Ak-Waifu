from telegram import Update
from telegram.ext import CallbackContext

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/games - List mini games\n"
        "Just mention 'Sakura' to chat with me!"
    )