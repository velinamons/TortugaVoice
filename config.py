from dotenv import load_dotenv
import os

environment_state = os.getenv('ENVIRONMENT_STATE')

if environment_state == 'LOCAL':
    load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', 'default_token_here')
