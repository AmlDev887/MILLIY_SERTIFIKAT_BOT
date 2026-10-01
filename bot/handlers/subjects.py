from app.models import Subject
from aiogram import Router,types,F
from aiogram.filters import Command
from app.database import SessionLocal
from sqlalchemy import select
from bot.keyboards.keybord_start import *
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
router = Router()

@router.message(F.text=="📚 Fanlar")
async def cmd_fan(message: types.Message):
    keyboard = []
    async with SessionLocal() as session:
        stmt = select(Subject).where(Subject.is_active == True)
        result = await session.execute(stmt)    
        users = result.scalars().all()
    for user in users:
        keyboard.append([KeyboardButton(text=user.name)])
    
    fan_keyboard = ReplyKeyboardMarkup(keyboard = keyboard)
    await message.answer("Fanni tanlang", reply_markup = fan_keyboard)


        

    