from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import time
import threading

url = "https://49b259f7070f2b79.mokky.dev/order"
bot_token = "7026538209:AAFbM-BipTmjC-GoforI8eoJwjD5fcBdOhE"

# Список пользователей, у которых есть бот
users_with_bot = []

# Функция-обработчик для команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Салам")
    if update.message.chat_id not in users_with_bot:
        users_with_bot.append(update.message.chat_id)
    thread = threading.Thread(target=check_orders)
    thread.start()

id_chek = 0
def check_orders() -> None:
    global id_chek
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            items = response.json()
            if not items:
                continue
            max_item = max(items, key=lambda x: x['id'])
            if max_item != id_chek:
                id_chek = max_item
                message = create_order_message(max_item)
                send_message_to_all_users(message)
        else:
            print("Не удалось получить данные.")
        
        # Задержка между запросами
        time.sleep(5)

def create_order_message(order_data) -> str:
    message = f"↓\n【З】【А】【К】【А】【З】 №{order_data['id']}\n\n"
    all_price = 0
    for i, item in enumerate(order_data["items"], start=1):
        name = item['title']
        price = item['price']
        message += f"Т̲о̲в̲а̲р̲: {i}\n     •Название товара: {name}\n     •Цена товара: {price} ₽\n\n"
        all_price += price
    message += f"\nО͟б͟щ͟а͟я͟ ͟с͟т͟о͟и͟м͟о͟с͟т͟ь͟ ͟з͟а͟к͟а͟з͟а͟,͟ ͟с͟о͟с͟т͟а͟в͟л͟я͟е͟т͟: {all_price} ₽"
    return message

def send_message_to_all_users(message: str) -> None:
    bot = Bot(token=bot_token)
    for user_id in users_with_bot:
        bot.send_message(chat_id=user_id, text=message)

def main() -> None:
    # Инициализация бота с токеном
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Старт работы бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
