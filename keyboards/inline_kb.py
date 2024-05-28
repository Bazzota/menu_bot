from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon_ru import lexicon_ru


def create_start_inline_kb():
    buttons = []
    for callback, text in lexicon_ru.start_inline_kb.items():
        inline_button = InlineKeyboardButton(text=text, callback_data=callback)
        buttons.append([inline_button])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def create_choose_menu_kb():
    buttons = []
    for callback, text in lexicon_ru.choose_menu_inline_kb.items():
        inline_button = InlineKeyboardButton(text=text, callback_data=callback)
        buttons.append([inline_button])
    return InlineKeyboardMarkup(inline_keyboard=buttons)