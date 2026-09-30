from app.config import BOT_TOKEN
from aiogram import Bot,Dispatcher
import asyncio
from bot.handlers import start
from bot.handlers import subjects

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(start.router)
    dp.include_router(subjects.router)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())