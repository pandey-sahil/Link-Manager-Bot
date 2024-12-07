# Use Python 3.9-slim-buster instead of Python 3.8
FROM python:3.9-slim-buster

# Update the system and install necessary dependencies
RUN apt update && apt upgrade -y
RUN apt install -y git

# Copy the requirements.txt into the container
COPY requirements.txt /requirements.txt

# Upgrade pip and install dependencies from requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Create the directory for the bot
RUN mkdir /converterbot
WORKDIR /converterbot

# Copy the start.sh script into the container
COPY start.sh /start.sh

# Run the bot with the start.sh script
CMD ["/bin/bash", "/start.sh"]
