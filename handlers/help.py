from telegram.ext import CallbackContext
from telegram import Update


async def help_cmd(update: Update, context: CallbackContext):
    """
     Reply to /help
    """
    msg = ("Just use the commands and I'll do the rest:"
           "\n/generate"
           "\n/check_strength"
           "\n\nMade by Arian Nemati🍓")

    await update.message.reply_text(msg)