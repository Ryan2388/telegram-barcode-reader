from telegram import Update
from telegram.ext import CallbackContext


def handle_unknown(update: Update, context: CallbackContext):
    del context  # Not used
    update.effective_chat.reply_text(
        "Sorry, I do not understand you. Try /start command"
    )
