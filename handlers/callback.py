from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InputMediaPhoto
from keyboards.inline import start_m1
from keyboards.inline import start_m2
from handlers.commands import about_message
from handlers.commands import help_handler
from handlers.commands import about_IS_hendler
from handlers.commands import criteria_hendler
from handlers.commands import about_info
from handlers.commands import examples
from handlers.commands import advice_handler
from keyboards.inline import first_details
from keyboards.inline import second_details
from keyboards.inline import third_details
from keyboards.inline import first_photos
from keyboards.inline import second_photos
from keyboards.inline import third_photos

callback_router = Router()


@callback_router.callback_query(F.data_in(['prev', 'next']))
async def start_callback(callback: CallbackQuery):
    if callback.data == 'next':
        await callback.message.edit_text(text="Привет! Я рад, что ты хочешь начать подготовку к итоговому сочинению, "
                                              "поэтому собираюсь помочь с выбором"
                                              "актуальных произведений для твоих аргументов 😉 \n"
                                              "Выбирай раздел и подраздел тем ИС, а я подберу для тебя произведения "
                                              "разных форматов 👌🏻"
                                              "Нажимай на нужную команду 👇🏻", reply_markup=start_m2)
    else:
        await callback.message.edit_text(
            text="Привет! Я рад, что ты хочешь начать подготовку к итоговому сочинению, поэтому собираюсь помочь с "
                 "выбором"
                 "актуальных произведений для твоих аргументов 😉 \n"
                 "Выбирай раздел и подраздел тем ИС, а я подберу для тебя произведения разных форматов 👌🏻"
                 "Нажимай на нужную команду 👇🏻", reply_markup=start_m1)
    await callback.answer()


@callback_router.callback_query(F.data == 'about_mes')
async def about_message_callback(callback: CallbackQuery):
    await callback.answer()
    await about_message(callback.message)


@callback_router.callback_query(F.data == 'help_mes')
async def help_handler_callback(callback: CallbackQuery):
    await callback.answer()
    await help_handler(callback.message)


@callback_router.callback_query(F.data == 'task_mes')
async def about_IS_hendler_callback(callback: CallbackQuery):
    await callback.answer()
    await about_IS_hendler(callback.message)


@callback_router.callback_query(F.data == 'criteria_mes')
async def criteria_hendler_callback(callback: CallbackQuery):
    await callback.answer()
    await criteria_hendler(callback.message)


@callback_router.callback_query(F.data == 'literature_mes')
async def about_info_callback(callback: CallbackQuery):
    await callback.answer()
    await about_info(callback.message)


@callback_router.callback_query(F.data == 'examples_essay_mes')
async def examples_callback(callback: CallbackQuery):
    await callback.answer()
    await examples(callback.message)


@callback_router.callback_query(F.data == 'advice_mes')
async def advice_handler_callback(callback: CallbackQuery):
    await callback.answer()
    await advice_handler(callback.message)


@callback_router.callback_query(F.data == 'first_chapter')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Духовно-нравственные ориентиры в жизни человека",
                                     reply_markup=first_details)


@callback_router.callback_query(F.data == 'second_chapter')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Семья, общество, Отечество в жизни человека \nВыбери подраздел 👇🏻",
                                     reply_markup=second_details)


@callback_router.callback_query(F.data == 'third_chapter')
async def third_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Природа и культура в жизни человека \nВыбери подраздел 👇🏻",
                                     reply_markup=third_details)


@callback_router.callback_query(F.data.in_(['first_1', 'second_1', 'third_1', 'fourth_1']))
async def first_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="<b>Что почитать:</b>\n\n\n"
                                          "<b><i>Небольшое, но универсальное:</i></b>\n\n"
                                          "    М. Шолохов «Судьба человека» (смысл жизни, нравственный выбор, добро и "
                                          "зло)\n\n"
                                          "    А. Толстой «Русский характер» (любовь, нравственный выбор, сила духа)\n\n"
                                          "    Антуан де Сент-Экзюпери «Маленький принц» (смысл жизни, ответственность, "
                                          "любовь, дружба)\n\n"
                                          "    М. Горький «Старуха Изергиль» (смысл жизни, гордость, свобода личная и "
                                          "свобода народа, ответственность)\n\n"
                                          "    Джек Лондон «Любовь к жизни» (предательство, сила духа)\n\n"
                                          "    А.П. Платонов «Юшка» (смысл жизни, нравственный выбор, добро и зло)\n\n"
                                          "    А. И. Куприн «Чудесный доктор» (добро и зло)\n\n"
                                          "    В. Астафьев «Конь с розовой гривой» (муки совести, нравственный выбор, "
                                          "самоанализ)\n\n"
                                          "    А.П. Чехов «Скрипка Ротшильда» (смысл жизни, муки совести, самоанализ)\n\n"
                                          "    А. Грин «Зелёная лампа» (смысл жизни, сила духа)\n\n"
                                          "    А. Грин «Алый паруса» (любовь, мечта, добро и зло)\n\n"
                                          "    О. Генри «Дары волхвов» (любовь)\n\n\n"
                                          "<b><i>Большое, но универсальное:</i></b>\n\n"
                                          "    А.С. Пушкин «Капитанская дочка» (смысл жизни, нравственный выбор, добро и "
                                          "зло, любовь)\n\n"
                                          "    В. Астафьев «Людочка» (нравственный выбор, добро и зло)\n\n\n"
                                          "<b><i>Фэнтези:</i></b>\n\n"
                                          "    Дж. Толкин «Властелин колец»\n\n"
                                          "    Дж. Толкин «Хоббит, или Туда и обратно» (школьная программа)\n\n"
                                          "    А. Сапковский «Ведьмак»\n\n"
                                          "    Дж. К. Роулинг «Гарри Поттер»",
                                     parse_mode='HTML', reply_markup=first_photos)


@callback_router.callback_query(F.data.in_(['first_2', 'second_2', 'third_2', 'fourth_2']))
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='<b>Что почитать:</b>\n\n\n'
                                          '<b><i>Небольшое, но универсальное:</i></b>\n\n'
                                          '    М. Шолохов «Судьба человека» (+1 раздел) (гражданская позиция, семейные '
                                          'ценности)\n\n'
                                          '    М. Горький «Старуха Изергиль» (+1 раздел) (принятие и неприятие личности '
                                          'обществом)\n\n'
                                          '    А.П. Платонов «Юшка» (+1 раздел) (неприятие личности обществом)\n\n'
                                          '    Н. С. Лесков «Левша» (гражданская позиция)\n\n'
                                          '    В. Астафьев «Фотография, на которой меня нет» (+1 раздел) (сохранение '
                                          'памяти)\n\n\n'
                                          '<b><i>Большое, но универсальное:</i></b>\n\n'
                                          '    А.С. Пушкин «Капитанская дочка» (+1 раздел) (семейные и общественные '
                                          'ценности, гражданская позиция)\n\n'
                                          '    Н. Гоголь «Тарас Бульба» (+1 раздел) (общественные ценности, гражданская '
                                          'позиция)\n\n\n'
                                          '<b><i>Не совсем универсальное, но тоже полезное:</i></b>\n\n'
                                          '    Б. Полевой «Повесть о настоящем человеке» (+1 раздел) (гражданская позиция)',
                                     parse_mode='HTML', reply_markup=second_photos)


@callback_router.callback_query(F.data.in_(['first_3', 'second_3', 'third_3', 'fourth_3']))
async def third_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='<b>Что почитать:</b>\n\n\n'
                                          '<b><i>Небольшое, но универсальное:</i></b>\n\n'
                                          '    Рэй Брэдбери «Вельд» (наука, технологии)\n\n'
                                          '    Рэй Брэдбери «Улыбка» (искусство, технологии)\n\n'
                                          '    А.П. Чехов «Скрипка Ротшильда» (искусство) (+ 1 направление)\n\n'
                                          '    Д.С. Лихачёв «Письма о добром и прекрасном» (Письмо девятнадцатое. КАК ГОВОРИТЬ?» (язык)\n\n'
                                          '    Нора Галь «Слово живое и мёртвое» (язык)\n\n\n'
                                          '<b><i>Большое, но полезное:</i></b>\n\n'
                                          '    В. Короленко «Слепой музыкант» (искусство)\n\n\n'
                                          '<b><i>Небольшие произведения:</i></b>\n\n'
                                          '    Рэй Брэдбери «Зелёное утро» (природа)\n\n\n'
                                          '<b><i>Антиутопии:</i></b>\n\n'
                                          '    О. Хаксли «О дивный новый мир» (наука, технологии)\n\n'
                                          '    М.А. Булгаков «Роковые яйца» (наука)\n\n'
                                          '    М.А. Булгаков «Собачье сердце» (наука)\n\n\n'
                                          '<b><i>Современные произведения:</i></b>\n\n'
                                          '    С. Алексиевич «Чернобыльская молитва. Хроника будущего» (природа, '
                                          'технологии)\n\n'
                                          '    Юваль Ной Харари «21 урок для XXI века» (2018 год) (природа, технологии) ('
                                          'ядерная война, изменение климата и потенциально опасные технологии, '
                                          'опасность выделения элиты, разрыв между реальным миром и виртуальным, '
                                          'иллюзия знания)\n\n'
                                          '    А. Курпатов «Четвёртая мировая война» (2018 год) (технологии) (потенциально '
                                          'опасные технологии + деградация человеческого мышления)',
                                     parse_mode="HTML", reply_markup=third_photos)


@callback_router.callback_query(F.data == 'arg_1')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='<b><i>Соответствие теме:</i></b>\n'
                                          'Данный критерий нацеливает на проверку содержания сочинения.'
                                          'Участник должен рассуждать на предложенную тему, выбрав путь ее раскрытия'
                                          'например, отвечает на вопрос, поставленный в теме, или размышляет над '
                                          'предложенной'
                                          'проблемой и т.п.).'
                                          '«Незачет» ставится только в случае, если сочинение не соответствует теме, '
                                          'в нем нет'
                                          'ответа на вопрос, поставленный в теме, или в сочинении не прослеживается '
                                          'конкретной цели'
                                          'высказывания. Во всех остальных случаях выставляется «зачет».',
                                     parse_mode="HTML")


@callback_router.callback_query(F.data == 'arg_2')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='<b><i>Аргументация. Привлечение литературного материала:</i></b>\n'
                                          'Данный критерий нацеливает на проверку умения строить рассуждение, '
                                          'доказывать'
                                          'свою позицию, формулируя аргументы и подкрепляя их примерами из '
                                          'опубликованных'
                                          'литературных произведений. Можно привлекать произведения устного народного '
                                          'творчества'
                                          '(за исключением малых жанров), художественную, документальную, мемуарную,'
                                          'публицистическую, научную и научно-популярную литературу (в том числе '
                                          'философскую,'
                                          'психологическую, литературоведческую, искусствоведческую), дневники, очерки,'
                                          'литературную критику и другие произведения отечественной и мировой '
                                          'литературы'
                                          '(достаточно опоры на один текст).'
                                          '«Незачет» ставится при условии, если сочинение не содержит аргументации, '
                                          'написано'
                                          'без опоры на литературный материал, или в нем существенно искажено '
                                          'содержание'
                                          'выбранного текста, или литературный материал лишь упоминается в работе ('
                                          'аргументы'
                                          'примерами не подкрепляются). Во всех остальных случаях выставляется «зачет».',
                                     parse_mode="HTML")


@callback_router.callback_query(F.data == 'arg_3')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='<b><i>Композиция и логика рассуждения:</i></b>\n'
                                          'Данный критерий нацеливает на проверку умения логично выстраивать '
                                          'рассуждение'
                                          'на предложенную тему. Участник должен выдерживать соотношение между '
                                          'тезисом и'
                                          'доказательствами.'
                                          '«Незачет» ставится при условии, если грубые логические нарушения мешают'
                                          'пониманию смысла сказанного или отсутствует тезисно-доказательная часть. '
                                          'Во всех'
                                          'остальных случаях выставляется «зачет».', parse_mode="HTML")


@callback_router.callback_query(F.data == 'arg_4')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='<b><i>Качество письменной речи:</i></b>\n'
                                          'Данный критерий нацеливает на проверку речевого оформления текста сочинения.'
                                          'Участник должен точно выражать мысли, используя разнообразную лексику и'
                                          'различные грамматические конструкции, при необходимости уместно '
                                          'употреблять термины.'
                                          '«Незачет» ставится при условии, если низкое качество речи (в том числе '
                                          'речевые'
                                          'ошибки) существенно затрудняет понимание смысла сочинения. Во всех '
                                          'остальных случаях'
                                          'выставляется «зачет».', parse_mode="HTML")


@callback_router.callback_query(F.data == 'arg_5')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='<b><i>Грамотность:</i></b>\n'
                                          'Данный критерий позволяет оценить грамотность выпускника.'
                                          '«Незачет» ставится при условии, если на 100 слов в среднем приходится в '
                                          'сумме более'
                                          'пяти ошибок: грамматических, орфографических, пунктуационных3.',
                                     parse_mode="HTML")


@callback_router.callback_query(F.data == 'soch_chd')
async def soch1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/8a207b9c-8a9f-4888-8f0e-babbb295c962/',
        caption='"Чудесный доктор"')


@callback_router.callback_query(F.data == 'soch_zel_lampa')
async def soch2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/414df2a4-26b2-40c5-823d-c08a92fa9f58/',
        caption='"Зеленая лампа"')


@callback_router.callback_query(F.data == 'soch_ushka')
async def soch3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/eb4bba50-0988-440f-ac56-58dedf933d3a/',
        caption='"Юшка"')


@callback_router.callback_query(F.data == 'soch_kon')
async def soch4(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/40b35acc-4af4-42bc-8a79-483ff3c09bed/',
        caption='"Конь с розовой гривой"')


@callback_router.callback_query(F.data == 'soch_love')
async def soch5(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/7b801758-7b21-4cea-bab8-0e41c39d9439/',
        caption='"Любовь к жизни"')


@callback_router.callback_query(F.data == 'soch_doch')
async def soch6(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/78b2b7ec-8e3f-4429-bc96-3e6f0441d19b/',
        caption='"Капитанская дочь"')


@callback_router.callback_query(F.data == 'soch_taras')
async def soch7(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/1171c201-1bd5-4d8d-b57a-a8a61a3f2ab3/',
        caption='"Тарас Бульба"')


@callback_router.callback_query(F.data == 'soch_chern')
async def soch8(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/0ad5b94f-546c-4c64-9790-ad5a780cb1d1/',
        caption='"Чернобыльская молитва"')


@callback_router.callback_query(F.data == 'soch_smile')
async def soch9(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/2f0e8f7d-7b39-4bc2-8fc1-c45168416914/',
        caption='"Улыбка" и "Зеленое утро"')


@callback_router.callback_query(F.data == 'soch_veld')
async def soch10(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/fc631358-3f88-4746-884b-92f3cd66d281/',
        caption='"Вельд" и "Четвёртая мировая война"')


@callback_router.callback_query(F.data == 'soch_rock')
async def soch11(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo='https://ucarecdn.com/28fc664b-1262-4018-9ee0-0981a6338d50/',
        caption='"Роковые яйца"')
