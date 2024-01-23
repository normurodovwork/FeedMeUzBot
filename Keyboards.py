from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

langs_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇿 O\'zbekcha'),
            KeyboardButton(text='🇷🇺 Русский'),
            KeyboardButton(text='🇬🇧 English'),
        ]
    ],
    resize_keyboard=True
)


'''Category'''

category_kb_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🍴 Меню')],
        [KeyboardButton(text='✍️ Оставить отзыв'), KeyboardButton(text='⚙️ Настройки')]
    ],
    resize_keyboard=True
)

category_kb_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🍴 Menu')],
        [KeyboardButton(text='✍️ Fikringizni qoldiring'), KeyboardButton(text='⚙️ Solamalar')]
    ],
    resize_keyboard=True
)

category_kb_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🍴 Menu')],
        [KeyboardButton(text='✍️ Give your feedback'), KeyboardButton(text='⚙️ Settings')]
    ],
    resize_keyboard=True
)

'''Geolocation'''


button_geo_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Manzilni yuborish", request_location=True)]
    ],
    resize_keyboard=True
)

button_geo_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить локацию", request_location=True)]
    ],
    resize_keyboard=True
)


button_geo_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Send location", request_location=True)]
    ],
    resize_keyboard=True
)

'''Phone number'''

button_phone_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Raqamni yuborish", request_contact=True)]
    ],
    resize_keyboard=True
)

button_phone_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить номер", request_contact=True)]
    ],
    resize_keyboard=True
)


button_phone_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Send contact", request_contact=True)]
    ],
    resize_keyboard=True
)
