import requests
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6092795077:AAEfFrIwXIGgYiWDKNwlaKxQ7W2jNAZ_KHQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(" Hi! I'm a translator bot. I translate into 5 languages and it's super fast! Enjoy the results!")


@dp.message_handler()
async def echo(message: types.Message):
    xabar = message.text 
    r = requests.get(f'https://trans.noxi8.repl.co/ru/text={xabar}')
    r2 = requests.get(f'https://trans.noxi8.repl.co/en/text={xabar}')
    r3 = requests.get(f'https://trans.noxi8.repl.co/fr/text={xabar}')
    r4 = requests.get(f'https://trans.noxi8.repl.co/tr/text={xabar}')
    r5 = requests.get(f'https://trans.noxi8.repl.co/uk/text={xabar}')
    response2=r2.json()['text']
    response = r.json()['text']
    response3 = r3.json()['text']
    response4 = r4.json()['text']
    response5 = r5.json()['text']
    await message.reply(f' 🇷🇺перевод: {response}\n🇺🇸translation: {response2}\n🇫🇷traduction: {response3}\n🇹🇷tercüme:  {response4}\n🇺🇦переклад: {response5}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
