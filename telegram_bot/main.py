from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5715310006:AAEXW2SNalz3lS2AZfRmE-dpstuLnH9YiiA'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет\nЯ - бот")
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 