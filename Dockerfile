# Используем базовый образ Python
FROM python:3.8-slim

# Устанавливаем системные зависимости
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в контейнер
WORKDIR /app
COPY . .

# Определяем переменную окружения для токена Telegram бота
ENV TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"

# Указываем порт, который будем использовать для webhook или для локального тестирования
EXPOSE 8443

# Запускаем бота
CMD ["python", "test.py"]
