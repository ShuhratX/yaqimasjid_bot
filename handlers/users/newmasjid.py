from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db
from states.newmosque import NewMosque



@dp.message_handler(Command("new", prefixes="!/"), user_id=ADMINS)
async def yangi_masjid(message: types.Message):
    await message.answer("Masjid ma'lumotlarini yuboring:")
    await NewMosque.YangiMasjid.set()

@dp.message_handler(state=NewMosque.YangiMasjid)
async def masjid_add(message: types.Message, state: FSMContext):
    try:
        name = message.text.split(", ")[0]
        latitude = message.text.split(", ")[1]
        longtitude = message.text.split(", ")[2]

        await db.create()
        count = await db.count_mosques()
        mosque = await db.add_mosque(
            name=name,
            latitude=latitude,
            longtitude=longtitude
        )
        javob = f"<b>{mosque[1]}</b> jome masjidi bazaga qo'shildi."
    except:
        javob = "Ma'lumotlar xato kiritildi"
    await message.answer(javob)
    await state.finish()

@dp.message_handler(Command("count", prefixes="!/"), user_id=ADMINS)
async def count_mosques(message: types.Message):
    await db.create()
    count = await db.count_mosques()
    javob = f"Masjidlar soni: {count} ta"
    await message.answer(javob)


@dp.message_handler(user_id=ADMINS)
async def delete(message: types.Message):
    await db.create()
    name = message.text.split("!delete ")[1]
    print(name)
    await db.delete_mosque(name)
    await message.answer(f"{name} jome masjidi o'chirildi.")


# @dp.message_handler(Command("mosques", prefixes="!/"), user_id=ADMINS)
# async def mosques(message: types.Message):
#     await db.create()
#     mosques = await db.get_mosques()
#     for mosque in mosques:
#         print(mosque[0])
#     # javob = f"Masjidlar soni: {count} ta"
#     await message.answer("Masjidlar chop qilindi")