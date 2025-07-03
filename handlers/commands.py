from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import Command, or_f
from keyboards.inline import about_kb
from keyboards.inline import criteria_doc
from keyboards.inline import examples_essay
from keyboards.inline import start_m1
from keyboards.inline import start_m2


command_router = Router()


@command_router.message(or_f(Command('start'), F.text == 'start'))
async def start_handler(message: Message):
    start_text = (
        "Привет! Я рад, что ты хочешь начать подготовку к итоговому сочинению, поэтому собираюсь помочь с выбором "
        "актуальных произведений для твоих аргументов 😉 \n"
        "Выбирай раздел и подраздел тем ИС, а я подберу для тебя произведения разных форматов 👌🏻"
        "Нажимай на нужную команду 👇🏻"
    )
    await message.answer(text=start_text, reply_markup=start_m1)


@command_router.message(or_f(Command('start'), F.text == 'start'))
async def start_handler(message: Message):
    start_text = (
        "Привет! Я рад, что ты хочешь начать подготовку к итоговому сочинению, поэтому собираюсь помочь с выбором "
        "актуальных произведений для твоих аргументов 😉 \n"
        "Выбирай раздел и подраздел тем ИС, а я подберу для тебя произведения разных форматов 👌🏻"
        "Нажимай на нужную команду 👇🏻"
    )
    await message.answer(text=start_text, reply_markup=start_m2)


@command_router.message(Command('about'))
async def about_message(message: Message):
    await message.answer(text="Я твой помощник в подготовке к итоговому сочинению по русскому языку! Помогу подобрать "
                             "произведения на любую тему 😌")


@command_router.message(Command('help'))
async def help_handler(message: Message):
    help_text = 'Нажми на эту команду и воспользуйся мной :) /start '
    await message.answer(text=help_text)


@command_router.message(Command('task'))
async def about_IS_hendler(message: Message):
    await message.answer(text='Выберите только ОДНУ из предложенных тем итогового сочинения, в бланке записи итогового'
                              'сочинения перепишите название выбранной темы сочинения.'
                              'Напишите сочинение-рассуждение на эту тему. Рекомендуемый объём − от 350 слов. Если в '
                              'сочинении менее 250 слов (в подсчёт включаются всеслова, в том числе и служебные),'
                              'то за такую работу ставится «незачёт». В рамках заявленной темы сформулируйте свою '
                              'позицию, докажитееё,'
                              'подкрепляя аргументы примерами из опубликованных литературных'
                              'произведений. Можно привлекать произведения устного народного творчества (за '
                              'исключением малых жанров), а также художественную, документальную,'
                              'мемуарную, публицистическую, научную и научно-популярную литературу (в том числе '
                              'философскую, психологическую, литературоведческую,'
                              'искусствоведческую), дневники, очерки, литературную критику и другие произведения '
                              'отечественной и мировой литературы.'
                              'Достаточно опоры на один текст (количество привлечённых текстов не так важно, '
                              'как глубина раскрытия темы с опорой на литературный материал).'
                              'Продумайте композицию сочинения. Соблюдайте речевые и орфографические нормы ('
                              'разрешается пользоваться орфографическим словарём).'
                              'Сочинение пишите чётко и разборчиво. При оценке сочинения в первую очередь учитывается '
                              'соблюдение требований объема и самостоятельности'
                              'написания сочинения, соответствие выбранной теме, умение аргументировать позицию и '
                              'обоснованно привлекать литературный материал.')


@command_router.message(Command('criteria'))
async def criteria_hendler(message: Message):
    await message.answer(text='Самые важные критерии:\n'
                              '- Соответствие теме\n'
                              '- Литературная аргументация\n'
                              '- Минимум 250 слов\n'
                              ' - Самостоятельность написания сочинения \n'
                              'Менее важные критерии\n '
                              '- Композиция\n'
                              '- Качество речи\n '
                              '- Грамотность\n'
                              'Выбирай критерий, с которым хочешь познакомиться подробнее:', reply_markup=criteria_doc)


@command_router.message(Command('literature'))
async def about_info(message: Message):
    about_text = "Ты вызвал команду /literature \nВыбирай раздел ИС 👇🏻 "
    await message.answer(text=about_text, reply_markup=about_kb)


@command_router.message(Command('examples_essay'))
async def examples(message: Message):
    await message.answer(text='Вот примеры сочинений по всем направлениям:', reply_markup=examples_essay)


@command_router.message(Command('advice'))
async def advice_handler(message: Message):
    await message.answer(text='📌 Советы по написанию:\n'
                              '❗️ Выберите тему, для которой у вас есть АРГУМЕНТ\n'
                              '❗️ Отталкивайтесь от аргумента, когда будете составлять тезис\n'
                              '❗️ Составьте план\n'
                              '- Пишите проще\n'
                              '- Тренируйтесь\n'
                              '- Не старайтесь учить чужие аргументы. В качестве тренировка лучше самостоятельно '
                              'написать 1 аргумент, чем выучить 10 чужих\n'
                              '- Не волнуйтесь, итоговое сочинение можно пересдать')


@command_router.message(F.text.lower().contains('пока'))
async def send_cute_message(message: Message):
    cute_text = 'До свидания)'
    await message.reply(text=cute_text)


@command_router.message(F.sticker)
async def react_to_sticker(message: Message):
    await message.reply(text='Классный стикер! 👍')


@command_router.message(F.photo)
async def react_to_photo(message: Message):
    await message.reply(text='Отличное фото!')


@command_router.message(F.reply_to_message & F.text.lower().contains('thank'))
async def react_to_reply(message: Message):
    await message.reply(text='да не за что:)')


@command_router.message()
async def echo_handler(message: Message):
    await message.reply(message.text)
