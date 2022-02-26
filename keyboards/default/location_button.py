from wsgiref.util import request_uri
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, 
                                keyboard=[
                                    [
                                        KeyboardButton(text="📍 Lokatsiya yuborish",
                                                            request_location=True)
                                    ]
                                ])