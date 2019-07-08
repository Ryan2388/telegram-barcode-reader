from telegram.ext import CommandHandler, MessageHandler, Filters

from .start import handle_start
from .recognize import handle_photo

HANDLERS = [
    CommandHandler("start", handle_start),
    MessageHandler(Filters.photo, handle_photo),
]
