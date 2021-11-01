import config
from aiogram import types, executor, Dispatcher, Bot

TOKEN = "2079683647:AAGX439vr8BZKhoSWmn6xoo8NRROmAClBlU"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, "Hi")

@dp.message_handler(content_types=["text"])
async def text(message: types.Message):
    if message.text.lower() == "пока":
        await message.reply("Досвидания")

#executor.start_polling(dp)