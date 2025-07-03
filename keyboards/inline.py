from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_m1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='/about', callback_data='about_mes')],
        [InlineKeyboardButton(text='/help', callback_data='help_mes')],
        [InlineKeyboardButton(text='/task', callback_data='task_mes')],
        [InlineKeyboardButton(text='/criteria', callback_data='criteria_mes')],
        [InlineKeyboardButton(text='➡️', callback_data='next')]
    ]
)

start_m2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='/literature', callback_data='literature_mes')],
        [InlineKeyboardButton(text='/examples_essay', callback_data='examples_essay_mes')],
        [InlineKeyboardButton(text='/advice', callback_data='advice_mes')],
        [InlineKeyboardButton(text='⬅️', callback_data='prev')]
    ]
)

about_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Духовно-нравственные ориентиры в жизни человека',
                              callback_data='first_chapter')],
        [InlineKeyboardButton(text='Семья, общество, Отечество в жизни человека',
                              callback_data='second_chapter')],
        [InlineKeyboardButton(text='Природа и культура в жизни человека',
                              callback_data='third_chapter')]
    ]
)

first_details = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Внутренний мир человека и его личностные качества.',
                              callback_data='first_1')],
        [InlineKeyboardButton(text='Отношение человека к другому человеку (окружению), нравственные идеалы и выбор '
                                   'между добром и злом.',
                              callback_data='second_1')],
        [InlineKeyboardButton(text='Познание человеком самого себя.',
                              callback_data='third_1')],
        [InlineKeyboardButton(text='Свобода человека и ее ограничения.',
                              callback_data='fourth_1')]

    ]
)

second_details = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Семья, род; семейные ценности и традиции',
                              callback_data='first_2')],
        [InlineKeyboardButton(text='Человек и общество.',
                              callback_data='second_2')],
        [InlineKeyboardButton(text='Родина, государство, гражданская позиция человека.',
                              callback_data='third_2')],

    ]
)

third_details = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Природа и человек.',
                              callback_data='first_3')],
        [InlineKeyboardButton(text='Наука и человек',
                              callback_data='second_3')],
        [InlineKeyboardButton(text='Искусство и человек.',
                              callback_data='third_3')],
        [InlineKeyboardButton(text='Язык и языковая личность.',
                              callback_data='fourth_3')]

    ]
)

criteria_doc = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Соответствие теме',
                              callback_data='arg_1')],
        [InlineKeyboardButton(text='Аргументация. Привлечение литературного материала',
                              callback_data='arg_2')],
        [InlineKeyboardButton(text='Композиция и логика рассуждения',
                              callback_data='arg_3')],
        [InlineKeyboardButton(text='Качество письменной речи',
                              callback_data='arg_4')],
        [InlineKeyboardButton(text='Грамотность',
                              callback_data='arg_5')]

    ]
)

examples_essay = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='"Духовно-нравственные ориентиры в жизни человека"',
                              url='https://ctege.info/duhovno-nravstvennyie-orientiryi-v-zhizni-cheloveka/')],
        [InlineKeyboardButton(text='"Семья, общество, Отечество в жизни человека"',
                              url='https://ctege.info/semya-obschestvo-otechestvo-v-zhizni-cheloveka/')],
        [InlineKeyboardButton(text='"Природа и культура в жизни человека"',
                              url='https://ctege.info/priroda-i-kultura-v-zhizni-cheloveka/')]
    ]
)

first_photos = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сочинение "Чудесный доктор"',
                              callback_data='soch_chd')],
        [InlineKeyboardButton(text='Сочинение "Зеленая лампа"',
                              callback_data='soch_zel_lampa')],
        [InlineKeyboardButton(text='Аргумент "Юшка"',
                              callback_data='soch_ushka')],
        [InlineKeyboardButton(text='Аргумент "Конь с розовой гривой"',
                              callback_data='soch_kon')],
        [InlineKeyboardButton(text='Аргумент "Любовь к жизни"',
                              callback_data='soch_love')]
    ]
)

second_photos = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Аргумент "Капитанская дочка"',
                              callback_data='soch_doch')],
        [InlineKeyboardButton(text='Аргумент "Тарас Бульба"',
                              callback_data='soch_taras')]
    ]
)

third_photos = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сочинение "Чернобыльская молитва"',
                              callback_data='soch_chern')],
        [InlineKeyboardButton(text='Сочинение "Улыбка" и "Зеленое утро"',
                              callback_data='soch_smile')],
        [InlineKeyboardButton(text='Сочинение "Вельд" и "Четвертая мировая война"',
                              callback_data='soch_veld')],
        [InlineKeyboardButton(text='Аргумент "Роковые яйца"',
                              callback_data='soch_rock')]
    ]
)
