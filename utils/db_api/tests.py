import asyncio

from utils.db_api.pgsql import Database


async def test():
    db = Database()
    await db.create()
    print("Ulanish...")
    mosques = await db.get_mosques()
    for ms in mosques:
    # print("Users jadvalini yaratamiz...")
    # await db.drop_users()
    # print("O'chirildi")
    #
    # await db.create_table_users()
    # print("Yaratildi")

    # print("Foydalanuvchilarni qo'shamiz")
    #
    # await db.add_user("anvar", "sariqdev", 123456789)
    # await db.add_user("olim", "olim223", 12341123)
    # await db.add_user("1", "1", 131231)
    # await db.add_user("1", "1", 23324234)
    # await db.add_user("John", "JohnDoe", 4388229)
    # print("Qo'shildi")
    #
    users = await db.select_all_users()
    # for user in users:
    #     print(f"Barcha foydalanuvchilar: {user[1]} \n")

    #
    # user = await db.select_user(id=5)
    # print(f"Foydalanuvchi: {user}")


loop = asyncio.get_event_loop()
loop.run_until_complete(test())