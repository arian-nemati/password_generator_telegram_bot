from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import TOKEN
from handlers import start, generate, check_strength, message, help_cmd, non_text


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(CommandHandler("check_strength", check_strength))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
    app.add_handler(MessageHandler(~filters.TEXT, non_text))

    print("Telegram Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
