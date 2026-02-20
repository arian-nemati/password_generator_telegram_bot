from telegram import Update
from telegram.ext import CallbackContext


async def start(update: Update, context: CallbackContext):
    msg = ("Hi my friend❤️ I'm a Telegram bot for generating passwords and check your passwords strength.\n\n"
           "Please use these commands:\n"
           "/generate\n"
           "/check_strength\n"
           "/help\n\n"
           "This bot is created by Arian Nemati")

    await update.message.reply_text(msg)