from telegram.ext import CommandHandler, MessageHandler, Filters

from bot.callbacks import sorry, start

HANDLERS = [
    CommandHandler("start", start.handle_start),
    MessageHandler(Filters.all, sorry.handle_unknown),
]
