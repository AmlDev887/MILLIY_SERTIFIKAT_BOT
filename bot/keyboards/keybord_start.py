from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Fanlar"), KeyboardButton(text="📝 Yangi test")],
        [KeyboardButton(text="🗂 Testlar ro'yxati"), KeyboardButton(text="📊 Mening natijalarim")],
        [KeyboardButton(text="💬 Yordam")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Bo'limni tanlang 👇",
)
