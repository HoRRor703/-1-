# Используем базовый образ Python
FROM python:3.8-slim

# Устанавливаем системные зависимости


# Устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в контейнер
WORKDIR /app
COPY . .

# Определяем переменную окружения для токена Telegram бота
ENV TELEGRAM_BOT_TOKEN="6527826296:AAFpjpjchnBeYjMZ9Y-Xzi6bIvmuEfXHgtg"



# Запускаем бота
CMD ["python", "test.py"]
