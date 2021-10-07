from telebot import TeleBot, types
from .settings import BOT_TOKEN
from admin_panel.models import TelegramUser

from .keyboards import generate_quiz_start_menu
bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    text = f"""Привет {first_name}!
Вас приветствует Бот-Викторина
Правила бота простые:
1. Бот авторизует вас. Для этого бот автоматически соберёт следующее данные:
    Имя
    Фамилию
    Имя пользователя
    Телеграм ID

2. Викторина начнётся, когда игрок нажмёт на кнопку "Начать викторину"
3. На каждый вопрос будет дано по 4 варианта ответа, в качестве кнопок
4. Вопрос не ограничен по времени
4. Нажимайте на кнопки, что бы ответить на вопрос. Иначе вам засчитается неверный ответ !
5. Выигрывает тот игрок который ответит правильно больше остальных игроков.
"""
    bot.send_message(chat_id, text=text)
    register_user(message)
    bot.send_message(chat_id, "Начать викторину ?", reply_markup=generate_quiz_start_menu())


def register_user(message):
    """Регистрация пользователей в БД FireStore"""
    telegram_id = message.chat.id
    user_name = message.chat.username
    first_name = message.chat.first_name
    last_name = message.chat.last_name

    user, created = TelegramUser.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
        username=user_name,
        telegram_id=telegram_id,
        defaults={"telegram_id", telegram_id},
    )

    print(user)
    bot.send_message(telegram_id, f"Авторизация прошла успешно {user}!")


@bot.message_handler(func=lambda message: "Начать викторину" in message.text)
def start_quiz(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Викторина началась !")
