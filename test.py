from telegram import Update
import textwrap
import numpy as np
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import g4f
# Замените на фактический токен вашего Telegram бота
TELEGRAM_BOT_TOKEN = "6527826296:AAFpjpjchnBeYjMZ9Y-Xzi6bIvmuEfXHgtg"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я твой помошник GPT703, к сожелению я не могу пока сохранять историю нашего диалога. Чем могу помочь?')

def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text  # Получение текста сообщения от пользователя
    # Using automatic a provider for the given model
## Streamed completion
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Ответь на русском:" + user_message}],
    stream=True,
)
    response_message = ""
    for message in response:
        response_message += message
      # Формирование ответа
    if len(response_message) > 4094:
        kol= len(response_message) // 4094
        update.message.reply_text(textwrap.wrap(response_message, kol+1))
    else:
        update.message.reply_text(response_message)  # Отправка ответа пользователю

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Обработка команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Обработка сообщений от пользователя
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()














