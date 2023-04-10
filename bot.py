import logging
from aiogram import Bot, Dispatcher, executor, types
from confing import TOKEN
from transliterate import translit
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}'
    logging.info(f'{user_name=}{user_id=}sent message: {message.text}')
    await message.reply(text)

@dp.message_handler()
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    ru_text = message.text
    text = translit(ru_text, language_code='ru', reversed=True)
    logging.info(f'{user_name=}{user_id=}sent message: {text}')
    await bot.send_message(user_id,text)

if __name__ == '__main__':
    executor.start_polling(dp)




#>>> from transliterate import translit
#>>> ru_text = 'Лорем ипсум долор сит амет'
#>>> text = translit(ru_text, language_code='ru', reversed=True)