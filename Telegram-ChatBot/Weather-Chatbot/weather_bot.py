import secrets_token
import requests
import telebot


# defining Telegram Bot API Token and Weather Token
telegram_token = secrets_token.weather_bot
open_weather_token = secrets_token.weather_api

bot = telebot.TeleBot(token=telegram_token)

# Applying message to start a bot


@bot.message_handler(commands=['start', 'hello', 'help', 'Hi', 'hi'])
def send_welcome(message):
    bot.reply_to(message, "Glad to hear you! I'm a weather bot for you today.\nYou can ask me about the current "
                          "temperature anywhere in the world. Just send me a location!")


@bot.message_handler(func=lambda msg: True)
def answer(message):
    user_location = message.text  # getting the location from users
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&appid={open_weather_token}"
    response = requests.get(url=api_url)
    data = response.json()
    print(data)

    # proving a valid location
    if response.status_code == 200:
        temperature = data["main"]["temp"]
        temperature_to_celsius = round(temperature - 273.15, 2)
        bot.reply_to(message, f"The temperature in {user_location} is {str(temperature_to_celsius)} °C")
    else:
        bot.reply_to(message, "Sorry, I could not find certain location. Please try again.")


bot.polling()
