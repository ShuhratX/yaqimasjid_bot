import asyncpg
from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp, db, bot
from data.config import ADMINS

@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    try:
        await db.create()
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}. Botdan foydalanish uchun /yaqinmasjid buyrug'ini kiriting!")

    # Adminga xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

@dp.message_handler(commands='yaqinmasjid')
async def bot_start(message: types.Message):
    await message.answer(f"O'zingizga yaqin masjidlarni topish uchun pastdagi <b>lokatsiya yuborish</b> tugmasini bosing!",
                            reply_markup=keyboard)


@dp.message_handler(content_types='location')
async def get_contact(message: Message):
    location = message.location
    await db.create()
    masjid_list = await choose_shortest(location)


    await message.answer(f"Rahmat. \n"
                         f"Sizga eng yaqin 3 ta masjidlar:\n")
    for name, distance, url, latitude, longtitude in masjid_list:
        await message.answer(f"<a href='{url}'>{name}</a> jome masjidi: {distance:.1f} km",
                disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())
        await message.answer_location(latitude=latitude,
                                      longitude=longtitude)

