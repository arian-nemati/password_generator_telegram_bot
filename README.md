# Telegram Password Generator Bot

A simple Telegram bot that helps you generate strong passwords and check their strength. The bot interacts with you step by step to customize your password preferences.

## Features

- Password Generator: Create a password with your chosen length and character types.
  - Choose password length (minimum 8 characters)
  - Include or exclude:
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Symbols
- Password Strength Checker: Evaluate the strength of any password you provide.
- Input Validation: Ensures only valid responses are accepted (e.g., numbers for length, y/n for options).
- Non-Text Handling: Alerts users if a non-text message is sent.

## Commands

- /start - Start interacting with the bot
- /generate - Generate a new password with custom options
- /check_strength - Check the strength of an existing password
- /help - Display help information

## How It Works

1. Use /generate to start generating a password.
2. The bot will ask for:
   - Password length
   - Whether to use uppercase letters
   - Whether to use lowercase letters
   - Whether to use numbers
   - Whether to use symbols
3. After all selections, the bot generates a secure password.
4. Use /check_strength to evaluate the strength of any password you provide.
5. 

## Folder Structure

```
Telegram_password_generator_bot/
│
├─ handlers/          # Command and message handlers
│  ├─ generate.py
│  ├─ message.py
│  ├─ check_strength.py
│  ├─ start.py
│  ├─ help.py
│
├─ services/          # Password generator and strength checker classes
│  ├─ password_generator.py
│
├─ utils/             # Utility functions and character constants
│  ├─ validation.py
│  ├─ constants.py
│
├─ config.py          # Bot token and configuration
├─ bot.py             # Main bot file
├─ requirements.txt   # Dependencies
└─ README.md          
```

## Dependencies

- python-telegram-bot
- Python 3.10+

Install via:
pip install python-telegram-bot

## Notes

- The bot uses secrets for secure random password generation.
- All interactions are stored temporarily in user_data during a session and cleared after password generation or strength checking.

