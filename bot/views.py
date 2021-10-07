from django.views import View
from django.http import HttpResponse

import requests
from .settings import BOT_TOKEN, WEBHOOK_URL


class WebhookBot(View):
    @staticmethod
    def get(request):
        delete_webhook = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?drop_pending_updates=True"
        requests.post(delete_webhook)

        set_webhook = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
        response = requests.post(set_webhook, params={
            "url": WEBHOOK_URL,
            "max_connections": 40,
            "drop_pending_updates": True
        })
        return HttpResponse(f"<h1>Webhook подключен: {WEBHOOK_URL}</h1>\n {response.json()}")

    def post(self, request):
        data = request.POST
