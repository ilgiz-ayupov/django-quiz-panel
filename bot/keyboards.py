from telebot import types


def generate_quiz_start_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_btn = types.KeyboardButton(text="Начать викторину")
    keyboard.add(start_btn)
    return keyboard


def generate_answer_options_menu(answer_options):
    answer_options = list(set(answer_options))
    buttons = [types.KeyboardButton(text=option) for option in answer_options]
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
    keyboard.add(buttons)
    return keyboard
