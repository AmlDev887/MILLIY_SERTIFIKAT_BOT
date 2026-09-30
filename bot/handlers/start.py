from app.models import Users
import asyncio
from aiogram import Router,types
from aiogram.filters import CommandStart
from app.config import BOT_TOKEN
from app.database import SessionLocal
from sqlalchemy import select
from app.models import User
router = Router()

WELCOME_TXT = """👋 <b>[Bot nomi]</b> botiga xush kelibsiz!

Bu yerda siz <b>Milliy Sertifikat</b> imtihoniga tayyorlanasiz: haqiqiy imtihon formatidagi testlarni yechasiz va natijangizni ko'rasiz.

<b>Botda nimalar bor:</b>
📚 Fanlar: [matematika, fizika, kimyo...]
📝 Imtihon sanalari bo'yicha testlar, har birida [N] ta savol
📊 Test yakunlangach natija
🗂 Barcha urinishlar va to'lovlar tarixi shaxsiy kabinetda

<b>Tariflar (30 kun):</b>
🔹 <b>5 000 UZS</b>: 1 ta fan, haftasiga 1 ta test
🔹 <b>25 000 UZS</b>: 2 ta fan, haftasiga 3 ta test
🔹 <b>50 000 UZS</b>: barcha fanlar, testlar cheklovsiz

<b>Qanday boshlash kerak:</b>
1. Fanni tanlang
2. Tarifni tanlang
3. To'lov qiling va chekni yuboring
4. Tekshiruvdan so'ng kirish huquqini oling

Savollar uchun: [@qo'llab-quvvatlash]"""

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(WELCOME_TXT, parse_mode = 'HTML')
    telegram_id = message.from_user.id
    user = await SessionLocal.scalar(
        select(User).where(User.telegram_id == telegram_id)
    )
    if not user:
        user = User(
            telegram_id = telegram_id,
            username = message.from_user.username,
            first_name = message.from_user.first_name
        )
    SessionLocal.add(user)
    await SessionLocal.commit()

