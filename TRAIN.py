import asyncioghbvth
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.commands import command_router
from handlers.callback import callback_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(command_router)
dp.include_router(callback_router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
