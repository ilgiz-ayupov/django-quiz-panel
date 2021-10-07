from telebot import types


def generate_quiz_start_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_btn = types.KeyboardButton(text="Начать викторину")
    keyboard.add(start_btn)
    return keyboard