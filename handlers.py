from datetime import datetime

from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from Database.models import feedback
from Database.database import database
from Keyboards import *

handlers_router = Router()

uz = '🇺🇿 O\'zbekcha'
ru = '🇷🇺 Русский'
en = '🇬🇧 English'


class Form(StatesGroup):
    language = State()
    category = State()
    menu = State()
    feedback = State()
    feedback_text = State()


@handlers_router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Form.language)
    await message.answer('Iltimos tilni tanglang\nПожалуйста выберите язык\nPlease choose language',
                         reply_markup=langs_kb)


@handlers_router.message(Form.language)
async def get_language(message: types.Message, state: FSMContext):
    await state.update_data(language=message.text)
    await state.set_state(Form.category)

    if message.text == uz:
        await message.answer('Kerakli bo\'limni tanglang', reply_markup=category_kb_uz)
    elif message.text == ru:
        await message.answer('Выберите нужный раздел', reply_markup=category_kb_ru)
    elif message.text == en:
        await message.answer('Choose category you need', reply_markup=category_kb_en)
    else:
        await message.answer('Choose category you need', reply_markup=category_kb_en)


@handlers_router.message(Form.category)
async def get_category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    data = await state.get_data()

    if '🍴' in message.text:

        await state.set_state(Form.menu)

        if data['language'] == uz:
            await message.answer('📍 Geolokatsiyani yuboring', reply_markup=button_geo_uz)
        elif data['language'] == ru:
            await message.answer('📍 Отправьте геолокацию', reply_markup=button_geo_ru)
        elif data['language'] == en:
            await message.answer('📍 Send geolocation', reply_markup=button_geo_en)

    elif '✍️' in message.text:

        await state.set_state(Form.feedback)

        if data['language'] == uz:
            await message.answer('📞 Raqamingizni yuboring', reply_markup=button_phone_uz)
        elif data['language'] == ru:
            await message.answer('📞 Отправьте номер', reply_markup=button_phone_ru)
        elif data['language'] == en:
            await message.answer('📞 Send contact', reply_markup=button_phone_en)


@handlers_router.message(Form.feedback)
async def get_feedback(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.contact.phone_number, name=message.contact.first_name)

    await state.set_state(Form.feedback_text)

    data = await state.get_data()
    if data['language'] == uz:
        await message.answer('Xabaringizni qoldiring')
    elif data['language'] == ru:
        await message.answer('Отправьте ваше сообщение')
    elif data['language'] == en:
        await message.answer('Send your message')


@handlers_router.message(Form.feedback_text)
async def feedback_text(message: types.Message, state: FSMContext):
    await state.update_data(message=message.text)
    data = await state.get_data()
    await save_feedback(data)
    await state.set_state(Form.category)
    await message.answer('Done')


async def save_feedback(db_data):
    query = feedback.insert().values(
        language=db_data['language'],
        name=db_data['name'],
        phone_number=db_data['contact'],
        message=db_data['message'],
        created_at=datetime.now()
    )
    await database.execute(query)
