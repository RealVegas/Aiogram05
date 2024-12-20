import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from loader import bot, dp, logger
from keyboards import section_keys


@dp.callback_query(F.data == 'dog_breed')
async def dog_breed(message: Message):
    await message.answer('Выберите породу собаки')


@dp.callback_query(F.data == 'space_photo')
async def space_photo(message: Message):
    https://api.nasa.gov/planetary/apod?NASA_API = DEMO_KEY
    await message.answer('Фото из Космоса', reply_markup=section_keys)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет! Я бот!')
    await message.answer('Выберите интересующий Вас раздел', reply_markup=section_keys)


@logger.catch
async def main():
    logger.info('Бот запущен')
    await dp.start_polling(bot)


async def stop_bot() -> None:
    await bot.session.close()
    logger.info('Бот остановлен')


if __name__ == '__main__':
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        asyncio.run(stop_bot())