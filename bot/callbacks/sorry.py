from telegram import Update
from telegram.ext import CallbackContext


def handle_unknown(update: Update, context: CallbackContext):
    del context  # Not used
    update.effective_message.reply_text(
        "Извини, я тебя не понимаю. Попробуй команду /start"
    )
