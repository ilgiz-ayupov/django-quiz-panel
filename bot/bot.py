import datetime

from telebot import TeleBot, types
from django.conf import settings
import psycopg2

from .settings import BOT_TOKEN
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
    try:
        register_user(message)
        bot.send_message(chat_id, "Начать викторину ?", reply_markup=generate_quiz_start_menu())
    except Exception as exp:
        print(exp.__class__.__name__, exp)


def register_user(message):
    """Регистрация пользователей в БД"""
    database = psycopg2.connect(
        host=settings.DATABASES["default"]["HOST"],
        database=settings.DATABASES["default"]["NAME"],
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"]
    )
    cursor = database.cursor()

    telegram_id = message.chat.id
    user_name = message.chat.username
    first_name = message.chat.first_name
    last_name = message.chat.last_name

    cursor.execute("""SELECT *
    FROM admin_panel_telegramuser
    WHERE telegram_id = %s
    """, (telegram_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("""
            INSERT INTO admin_panel_telegramuser 
            (
                first_name, last_name, username, telegram_id, true_answer, false_answer,
                current_question, status, duration_game
            ) 
            VALUES (%s, %s, %s, %s, 0, 0, 0, 'Авторизовался', 0)
        """, (first_name, last_name, user_name, telegram_id))

        database.commit()
        bot.send_message(telegram_id, "Регистрация прошла успешно!")
    else:
        bot.send_message(telegram_id, "Авторизация прошла успешно!")
    database.close()


@bot.message_handler(func=lambda message: "Начать викторину" in message.text)
def start_quiz(message: types.Message):
    chat_id = message.chat.id

    # Обновление состояния пользователя:
    #   Время начала викторины
    #   Статус : Проходит викторину

    start_game = datetime.datetime.now()

    database = psycopg2.connect(
        host=settings.DATABASES["default"]["HOST"],
        database=settings.DATABASES["default"]["NAME"],
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"]
    )
    cursor = database.cursor()

    cursor.execute("""UPDATE admin_panel_telegramuser
        SET start_game = %s,
        status = 'Проходит викторину'
        WHERE telegram_id = %s
    """, (start_game, chat_id))

    database.commit()
    database.close()
    bot.send_message(chat_id, "Викторина началась !")
