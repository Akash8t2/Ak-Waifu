from telegram import Update
from telegram.ext import CallbackContext
from games import get_truth, get_dare, roll_dice, toss_coin, rock_paper_scissors

def game_handler(update: Update, context: CallbackContext):
    msg = "Games: /truth /dare /dice /coin /rps"
    update.message.reply_text(msg)