from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder

Inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Задать запрос', callback_data='callback')]])