# Imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# Variables
updater = Updater(token='1081551554:AAESH4Fcy8UGCprG45jqP3mTxh_FshNZWdM', use_context=True)
dispatcher = updater.dispatcher

# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="A movie a day keeps the doctor away!")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
def setDate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="temp")
def YourMovie(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="temp")
    
# Main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

date_handler = CommandHandler('setDate', setDate)
dispatcher.add_handler(date_handler)

movie_handler = CommandHandler('YourMovie', YourMovie)
dispatcher.add_handler(movie_handler)

updater.start_polling()
print ("Bot is working")


