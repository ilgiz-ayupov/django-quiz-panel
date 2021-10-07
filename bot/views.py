from telebot import TeleBot, types
from rest_framework.response import Response
from rest_framework.views import APIView
from .settings import BOT_TOKEN, WEBHOOK_URL

from django.http import HttpResponse
from django.views import View

bot = TeleBot(BOT_TOKEN)


class UpdateBot(APIView):
    @staticmethod
    def post(request):
        json_str = request.body.decode("UTF-8")
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return Response({"code": 200})


class WebhookBot(View):
    def get(self, request):
        print("Бот запущен !")
        bot.delete_webhook(drop_pending_updates=True)
        response = bot.set_webhook(url=WEBHOOK_URL)
        if response:
            return HttpResponse(f"<h1>Бот запущен !</h1><p>{WEBHOOK_URL}</p>")
        return HttpResponse("<h1>Ошибка запуска</h1>")


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hello !")
