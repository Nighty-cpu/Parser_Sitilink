import asyncio
from aiogram import Bot,Dispatcher
import os
from dotenv import load_dotenv
from handlers import router
import logging

async def main():
    await dp.start_polling(bot)

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(router)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователем")
#проверка коммита

