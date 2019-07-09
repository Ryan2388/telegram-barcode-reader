from telegram.ext import CommandHandler, MessageHandler, Filters

from bot.callbacks import sorry, start, recognize

HANDLERS = [
    CommandHandler("start", start.handle_start),
    MessageHandler(Filters.photo, recognize.handle_photo),
    MessageHandler(Filters.all, sorry.handle_unknown),
]
