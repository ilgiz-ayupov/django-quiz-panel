from django.urls import path

from .views import UpdateBot, WebhookBot
from .settings import BOT_TOKEN

urlpatterns = [
    path("webhook/", WebhookBot.as_view(), name="webhook"),
    path(f"webhook{BOT_TOKEN}/", UpdateBot.as_view(), name="update")
]
