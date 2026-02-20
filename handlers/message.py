from telegram import Update
from telegram.ext import CallbackContext
from utils import is_valid_number, is_valid_yes_no
from services import PasswordPolicy, PasswordGenerator
from services import check


async def message(update: Update, context: CallbackContext):
    step = context.user_data['step']

    if not step:
        msg = ("Sorry❤️ I can't understand anything but these commands:\n\n"
              "/generate\n"
              "/check_strength\n"
              "/help")

        await update.message.reply_text(msg)
        return


    if step == "length":
        text = update.message.text

        if not is_valid_number(text):
            await update.message.reply_text("Please enter a valid number >= 8")
            return

        context.user_data['length'] = int(text)
        context.user_data['step'] = "upper"

        await update.message.reply_text("Do you want to use Uppercase (y/n): ")
        return


    if step == "upper":
        text = update.message.text

        if not is_valid_yes_no(text):
            await update.message.reply_text("Please answer y or n.")
            return

        context.user_data['upper'] = text in ["y", "yes"]
        context.user_data['step'] = "lower"

        await update.message.reply_text("Do you want to use Lowercase (y/n): ")
        return


    if step == "lower":
        text = update.message.text

        if not is_valid_yes_no(text):
            await update.message.reply_text("Please answer y or n.")
            return

        context.user_data['lower'] = text in ["y", "yes"]
        context.user_data['step'] = "number"

        await update.message.reply_text("Do you want to use Numbers (y/n): ")
        return


    if step == "number":
        text = update.message.text

        if not is_valid_yes_no(text):
            await update.message.reply_text("Please answer y or n.")
            return

        context.user_data['number'] = text in ["y", "yes"]
        context.user_data['step'] = "symbol"

        await update.message.reply_text("Do you want to use Symbols (y/n): ")
        return



    if step == "symbol":
        text = update.message.text

        if not is_valid_yes_no(text):
            await update.message.reply_text("Please answer y or n.")
            return

        context.user_data['symbol'] = text in ["y", "yes"]

        if not (context.user_data['upper'] or context.user_data['lower'] or
                context.user_data['number'] or context.user_data['symbol']) :
            await update.message.reply_text("At least one character must be provided!")
            context.user_data.clear()
            return

        policy = PasswordPolicy(
            length=context.user_data['length'],
            use_upper=context.user_data['upper'],
            use_lower=context.user_data['lower'],
            use_numbers=context.user_data['number'],
            use_symbols=context.user_data['symbol'],
        )

        generator = PasswordGenerator(policy)

        password = generator.generate()

        await update.message.reply_text(f"Here is your password: {password}")

        context.user_data.clear()
        return


    if step =="check_strength":
        text = update.message.text

        strength = check(text)
        await update.message.reply_text(f"Your password is {strength}!")


async def non_text(update: Update, context: CallbackContext):
    await update.message.reply_text("Sorry I can't answer anything but commands!❤️\nUse /help")