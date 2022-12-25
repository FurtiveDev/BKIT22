from currencies import *
from aiogram import Bot, Dispatcher, executor, types
TOKEN = '5922897666:AAGaU-deeg5XwCA1-BTxROwVbxCrrAHCgO4'
HELP_COMMAND = """
<b>/start</b> - <em>начать работу с ботом</em>
<b>/help</b> - <em>помощь</em>
<em>Чтобы посмотреть цены продажи валюты на данный момент, введите, к примеру, ltc_btc (лайткоин к биткоину).
Внимание, если бот не отвечает - значит в базе данных нет введенных валют или стоит поменять их местами (Например: btc_ltc вместо ltc_btc)</em>"""
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://yablyk.com/wp-content/uploads/2020/03/business-handshake.jpg")
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://s0.rbk.ru/v6_top_pics/media/img/2/21/756432988305212.jpg")
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    await message.reply(f"<em>Hello, {user_name}, this bot shows currencies sell prices. Enter /help to get more info</em>", parse_mode='HTML')
    await message.delete()


@dp.message_handler()
async def help_handler(message: types.Message):
    answ = get_data(message.text)
    if type(answ)==None:
        await message.reply(f'Извините, возможно такая команда не была предусмотрена, убедитесь, что всё ввели правильно'
                            f'(Пример:ltc_btc (лайткоин к биткоину) или попробуйте поменять валюты местами: btc_ltc (биткоин к лайткоину')
    else:
        await message.reply(text=answ)


if __name__ == '__main__':
    # get_data("usd_btc")
    executor.start_polling(dp)
