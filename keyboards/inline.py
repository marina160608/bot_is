from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

about_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='1. Духовно-нравственные ориентиры в жизни человека',
                              callback_data='first_chapter')],
        [InlineKeyboardButton(text='2. Семья, общество, Отечество в жизни человека', callback_data='second_chapter')],
        [InlineKeyboardButton(text='3. Природа и культура в жизни человека', callback_data='third_chapter')]
    ]
)

first_details = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Внутренний мир человека и его личностные качества.', callback_data='first_1')],
        [InlineKeyboardButton(
            text='Отношение человека к другому человеку (окружению), нравственные идеалы и выбор между добром и злом.',
            callback_data='second_1')],
        [InlineKeyboardButton(text='Познание человеком самого себя.', callback_data='third_1')],
        [InlineKeyboardButton(text='Свобода человека и ее ограничения.', callback_data='fourth_1')]

    ]
)

second_details = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Семья, род; семейные ценности и традиции', callback_data='first_2')],
        [InlineKeyboardButton(text='Человек и общество.', callback_data='second_2')],
        [InlineKeyboardButton(text='Родина, государство, гражданская позиция человека.', callback_data='third_2')],

    ]
)

third_details = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Природа и человек.', callback_data='first_3')],
        [InlineKeyboardButton(text='Наука и человек', callback_data='second_3')],
        [InlineKeyboardButton(text='Искусство и человек.', callback_data='third_3')],
        [InlineKeyboardButton(text='Язык и языковая личность.', callback_data='fourth_3')]

    ]
)

criteria_doc = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Критерии ФИПИ', url='https://doc.fipi.ru/itogovoe-sochinenie/2024'
                                                        '/04_Kriterii_it_soch.pdf')]

    ]
)
