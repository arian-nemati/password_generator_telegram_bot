from telegram import Update
from telegram.ext import CallbackContext


async def generate(update: Update, context: CallbackContext):
    context.user_data.clear()
    context.user_data['step'] = "length"

    await update.message.reply_text("Enter password length (a Number >= 8): ")
