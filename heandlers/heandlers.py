from aiogram import F, Router,Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from lexicon_ru import lexicon_ru
from keyboards import inline_kb
from config import main_config

router = Router()


@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text=lexicon_ru.text_commands['start'], reply_markup=inline_kb.create_start_inline_kb())


@router.callback_query(F.data == 'menu')
async def process_menu(callback: CallbackQuery):
    await Bot(main_config.tg_bot.token).send_message(chat_id=callback.from_user.id,
                                                     text='Выберите время приема пищи или меню на день',
                                                     reply_markup=inline_kb.create_choose_menu_kb())