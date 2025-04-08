from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN
from handlers.help_handler import help_command
from handlers.game_handler import game_handler
from handlers.chat_handler import chat_handler

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", help_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("games", game_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
