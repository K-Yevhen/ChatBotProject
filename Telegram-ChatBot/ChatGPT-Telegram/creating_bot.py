import openai

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import secrets_token

token = secrets_token.telegram_token
openai.api_key = secrets_token.open_ai_token

bot = Bot(token)
dispatcher = Dispatcher(bot)

# print(openai.Model.list())


@dispatcher.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    await message.answer(response['choices'][0]['text'])

executor.start_polling(dispatcher, skip_updates=True)
