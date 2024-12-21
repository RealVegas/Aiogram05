import asyncio
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from loader import bot, dp, logger
from keyboards import section_keys
from third_party import SpacePhoto, DogBreed


@dp.callback_query(F.data == 'dog_breed')
async def dog_breed(message: Message):
    await message.answer('Ожидаю ввода данных...')
    await bot.send_message(chat_id=message.from_user.id, text='Введите название породы собаки')
    bred = DogBreed().breed_pool()
    # await bot.send_message(chat_id=message.from_user.id, text=bred)


@dp.callback_query(F.data == 'space_photo')
async def space_photo(message: Message):
    await message.answer('Получаю данные...')
    nasa_photo, nasa_title = SpacePhoto().get_photo()
    await bot.send_photo(chat_id=message.from_user.id, photo=nasa_photo, caption=nasa_title)


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