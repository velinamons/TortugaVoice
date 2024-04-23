import config
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

class TelegramBot:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        self._add_command_handlers()

    def _add_command_handlers(self):
        self.application.add_handler(CommandHandler('start', self.start))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello, {user.first_name}! Welcome to our Telegram bot."
        )

    def run(self):
        self.application.run_polling()

if __name__ == "__main__":
    bot = TelegramBot(config.TELEGRAM_TOKEN)
    bot.run()
