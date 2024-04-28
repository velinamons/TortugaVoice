# TortugaVoice
TortugaVoice is a Telegram bot designed to perform various tasks. Currently, it supports a calculation feature, allowing users to send mathematical expressions for evaluation. We're also working on a voice-to-text implementation to expand its capabilities.

## Description
TortugaVoice enables users to interact with the bot via text messages, allowing them to send commands for mathematical calculations. The bot returns the calculated result in a user-friendly format.

## Installation
To set up the bot, follow these steps:

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**:
   ```bash
   TELEGRAM_TOKEN='YOUR_TELEGRAM_TOKEN'
   ```

3. **Run the Bot**:
   ```bash
   python main.py
   ```


## Usage
After setting up the bot, you can interact with it using the following commands:

- `/start`: Greets the user and initializes the bot.
  ```bash
  /start
  # Output: Hello, <user's first name>! Welcome to our Telegram bot.
  ```

- `/calculate <expression>`: Evaluates a mathematical expression and returns the result.
  ```bash
  /calculate 1 + 2 - 3 plus 4
  # Output: Calculated with result: 4
  ```

### Message Processing
In addition to commands, the bot can process text messages containing the keyword "calculate." It evaluates expressions that follow this keyword, even if it's not used as a command.

```bash
# Examples of message processing:
Please calculate 5 minus 7
# Output: Calculated with result: -2

Can you /calculate 5 minus 7
# Output: Calculated with result: -2
```

## Features
- **Calculation**: The bot evaluates mathematical expressions and returns the result.
- **Logging**: Uses `loguru` for structured logging, providing useful information for debugging and monitoring.
- **Upcoming Features**: Voice-to-text implementation for additional functionality.

## Contributors
- [velinamons](https://github.com/velinamons) - Initial development and ongoing work.

## License
This project is licensed under [MIT License](https://github.com/velinamons/TortugaVoice?tab=MIT-1-ov-file). Please refer to the license file for more information.
