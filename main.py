from telegram import Update
from telegram.ext import (    Application, CommandHandler, MessageHandler, filters,ConversationHandler, CallbackQueryHandler, CallbackContext)
import os
from dotenv import load_dotenv
from src.start import start as start_command
from src.addnewword import add_word_conversation_handler
from src.learn import learn, handle_translation_choice
from src.list import list_words
from src.practice import practice, handle_practice_choice, send_practice_word


load_dotenv('token.env')
BOT_TOKEN = os.getenv('BOT_TOKEN')

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Здесь добавляются остальные обработчики команд
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(add_word_conversation_handler)
    application.add_handler(CommandHandler('learn', learn))
    application.add_handler(CallbackQueryHandler(handle_translation_choice, pattern='^learn_'))
    application.add_handler(CommandHandler('list', list_words))
    application.add_handler(CommandHandler('practice', practice))
    application.add_handler(CallbackQueryHandler(handle_practice_choice))

    application.run_polling() #error

if __name__ == '__main__':
    main()