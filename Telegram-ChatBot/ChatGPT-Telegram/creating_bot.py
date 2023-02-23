import openai

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = "5849801643:AAGHnfrc6CNG4bRG8ztlhnIx6a9dQgaIiIs"
openai.api_key = "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"

bot = Bot(token)
dispatcher = Dispatcher(bot)

print(openai.Model.list())
