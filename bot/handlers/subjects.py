from app.models import Subject
from aiogram import Router,types
from aiogram.filters import Command
from app.database import SessionLocal
from sqlalchemy import select
from bot.keyboards.keybord_start import *
router = Router()

buttons = []
@router.message(Command("Fanlar"))
async def cmd_fan(message: types.Message):
    with SessionLocal() as session:
        stmt = select(Subject).where(Subject.is_active == True)
        result = session.execute(stmt)
        users = result.scalars().all()

        for user in users:
            buttons.append(user)
        await message.answer("Fanni tanlang", reply_markup = fan_keyboard)

        

    