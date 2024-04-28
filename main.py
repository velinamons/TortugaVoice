import re

from logger_config import logger
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler

import config
from enums import TGBotCommands


class TelegramBot:
    README_LINK = "https://github.com/velinamons/TortugaVoice?tab=readme-ov-file#usage"
    UNPROCESSABLE_CONTEXT_MSG = f"Unprocessable context, read details at [TortugaVoice]({README_LINK})"

    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        self._add_command_handlers()

    def _add_command_handlers(self):
        self.application.add_handler(CommandHandler(TGBotCommands.START.value, self.start))
        self.application.add_handler(CommandHandler(TGBotCommands.CALCULATE.value, self.calculate))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello, {user.first_name}! Welcome to our Telegram bot."
        )
        context.user_data["has_started"] = True
        logger.info("Starting the Telegram bot")

    async def calculate(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        result = self.UNPROCESSABLE_CONTEXT_MSG
        if context.user_data.get("has_started"):
            text = update.message.text
            logger.info(f"Received text: {text}")

            keyword_pos = text.find(TGBotCommands.CALCULATE.value)
            expression = text[keyword_pos + len(TGBotCommands.CALCULATE.value):].strip()
            result = self._calculate_expression(expression)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=result,
            parse_mode="MarkdownV2"
        )

    def _calculate_expression(self, expression: str) -> str:
        expression = expression.replace("plus", "+").replace("minus", "-")
        valid_expression = "".join(re.findall(r"[\d]+|[-+]", expression))
        try:
            result = eval(valid_expression)
            return f"Calculated with result: {result}"
        except Exception:
            return self.UNPROCESSABLE_CONTEXT_MSG

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text

        for keyword in TGBotCommands:
            command = keyword.value
            if command in text:
                await getattr(self, command)(update, context)
                break
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=self.UNPROCESSABLE_CONTEXT_MSG,
                parse_mode="MarkdownV2"
            )

    def run(self):
        self.application.run_polling()


def main():
    bot = TelegramBot(config.TELEGRAM_TOKEN)
    bot.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
