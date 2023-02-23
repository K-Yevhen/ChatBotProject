import secrets_token
import requests
import telebot


# defining Telegram Bot API Token and Weather Token
telegram_token = secrets_token.weather_bot
open_weather_token = secrets_token.weather_api

bot = telebot.TeleBot(token=telegram_token)

# Applying message to start a bot
@bot.message_handler(commands=['start', 'help', 'ask'])
def send_welcome(message):
    bot.reply_to(message, "Glad to hear you! I'm a weather bot for you today.\nYou can ask me about the current "
                          "temperature anywhere in the world. Just send me a location!")

@bot.message_handler()