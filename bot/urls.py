from django.urls import path

from .views import WebhookBot

urlpatterns = [
    path("webhook/", WebhookBot.as_view(), name="bot")
]
