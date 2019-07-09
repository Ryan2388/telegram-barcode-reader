from telegram import Update
from telegram.ext import CallbackContext

import bot
from bot import model


# Imaginary attacker can start bot with something other than `/start` via
#  MTProto and raise exception somewhere(interaction with db), but who cares?
def handle_start(update: Update, context: CallbackContext):
    del context  # Not used
    update.effective_chat.send_message("Hello world!")
    session = bot.Session()
    user = (
        session.query(model.User)
        .filter_by(ext_user_id=update.effective_user.id)
        .first()
    )
    if not user:
        user = model.User(ext_user_id=update.effective_user.id)
        session.add(user)
        session.commit()

    bot.Session.remove()
