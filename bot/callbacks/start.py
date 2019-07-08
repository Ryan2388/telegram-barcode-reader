from telegram import Update, ParseMode
from telegram.ext import CallbackContext


def handle_start(update: Update, context: CallbackContext):
    update.effective_chat.send_message(
        "Здравствуй! Я помогу распознать QR коды и другие баркоды.\n\n"
        "*Для распознования отправьте мне фотографию.*",
        parse_mode=ParseMode.MARKDOWN,
    )
