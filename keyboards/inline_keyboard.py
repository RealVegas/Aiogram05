from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Формирование клавиатуры выбора раздела
section_keys = InlineKeyboardMarkup(inline_keyboard=[[
                InlineKeyboardButton(text='Породы собак', callback_data='dog_breed'),
                InlineKeyboardButton(text='Просторы космоса', callback_data='space_photo')
                ]],
                row_width=1,
                resize_keyboard=True)