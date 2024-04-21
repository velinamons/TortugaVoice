from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load the .env file to read environment variables
load_dotenv()

# Get the Telegram bot token from the environment variable
telegram_token = os.getenv('TELEGRAM_TOKEN')

# Define a command handler for the '/start' command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello, {user.first_name}! Welcome to our Telegram bot."
    )

# Define the main function to run the Telegram bot
def main():
    # Initialize the Telegram bot with the token
    application = Application.builder().token(telegram_token).build()

    # Add a handler for the '/start' command
    application.add_handler(CommandHandler('start', start))

    # Start the bot to poll for messages
    application.run_polling()

# Entry point for the script
if __name__ == "__main__":
    main()
