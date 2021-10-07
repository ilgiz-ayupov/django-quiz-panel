from telebot import TeleBot, types
from django.conf import settings
import psycopg2

from .settings import BOT_TOKEN
from .keyboards import generate_quiz_start_menu

bot = TeleBot(BOT_TOKEN)
database = psycopg2.connect(
    host=settings.DATABASES["default"]["HOST"],
    database=settings.DATABASES["default"]["NAME"],
    user=settings.DATABASES["default"]["USER"],
    password=settings.DATABASES["default"]["PASSWORD"]
)
cursor = database.cursor()


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
    """Регистрация пользователей в БД"""
    telegram_id = message.chat.id
    user_name = message.chat.username
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    print("Начало регистрации ...")
    print("БАЗА ДАННЫХ ", settings.DATABASES["default"])

    cursor.execute("""SELECT *
    FROM telegramuser
    WHERE telegram_id = %s
    """, (telegram_id, ))
    user = cursor.fetchone()
    if not user:
        cursor.execute("""
            INSERT INTO telegramuser (first_name, last_name, username, telegram_id) 
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, user_name, telegram_id))
        bot.send_message(telegram_id, "Регистрация прошла успешно!")
    else:
        bot.send_message(telegram_id, "Авторизация прошла успешно!")


@bot.message_handler(func=lambda message: "Начать викторину" in message.text)
def start_quiz(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Викторина началась !")
