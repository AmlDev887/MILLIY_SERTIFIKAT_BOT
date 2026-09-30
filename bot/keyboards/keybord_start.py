from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.handlers.subjects import buttons
keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Fanlar"), KeyboardButton(text="📝 Yangi test")],
        [KeyboardButton(text="🗂 Testlar ro'yxati"), KeyboardButton(text="📊 Mening natijalarim")],
        [KeyboardButton(text="💬 Yordam")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Bo'limni tanlang 👇",
)

fan_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = button)]
        for button in buttons
    ]
)