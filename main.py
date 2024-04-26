import config
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from commands import Commands
import re

class TelegramBot:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        self._add_command_handlers()

    def _add_command_handlers(self):
        self.application.add_handler(CommandHandler(Commands.START.value, self.start))
        self.application.add_handler(CommandHandler(Commands.CALCULATE.value, self.calculate))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello, {user.first_name}! Welcome to our Telegram bot."
        )
        context.user_data["has_started"] = True

    async def calculate(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.user_data.get("has_started"):
            text = update.message.text
            print(text)
            keyword = "calculate"
            keyword_pos = text.find(keyword)
            expression = text[keyword_pos + len(keyword):].strip()
            print(context.args, expression)
            result = self.calculate_expression(expression)
        else:
            result="Unprocessable context, read comments at [some_link]"

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=result
        )

    def calculate_expression(self, expression: str) -> str:
        expression = expression.replace("plus", "+").replace("minus", "-")
        valid_expression = "".join(re.findall(r"[\d]+|[-+]", expression))
        try:
            result = eval(valid_expression)
            return f"Calculated with result: {result}"
        except Exception:
            return "Unprocessable context, read comments at [some_link]"

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text

        keyword = "calculate"
        if keyword in text:
            await self.calculate(update, context)
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Please use a command to interact with the bot."
            )

    def run(self):
        self.application.run_polling()

if __name__ == "__main__":
    bot = TelegramBot(config.TELEGRAM_TOKEN)
    bot.run()
