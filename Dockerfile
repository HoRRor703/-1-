
# Use the official image as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary dependencies
RUN pip install --no-cache-dir python-telegram-bot openai g4f
EXPOSE 8080 1337
# Specify the command to run on container start
CMD ["python", "test.py"]
