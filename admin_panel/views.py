from django.shortcuts import render
from django.views.generic import ListView
from .models import TelegramUser, Questions


class UsersList(ListView):
    model = TelegramUser
    template_name = "admin_panel/users_list.html"
    queryset = TelegramUser.objects.all()
    context_object_name = "user_list"

