from telegram import Update
from telegram.ext import CallbackContext


async def check_strength(update: Update, context: CallbackContext):
    context.user_data['step'] = "check_strength"

    await update.message.reply_text("Enter your password:")