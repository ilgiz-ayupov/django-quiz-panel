from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views import View
from .models import TelegramUser, Questions
from django.contrib import messages

from .forms import QuestionsForm


class UsersListView(ListView):
    model = TelegramUser
    template_name = "admin_panel/users_list.html"
    queryset = TelegramUser.objects.all()
    context_object_name = "users_list"
    extra_context = {
        "title": "Главаная страница"
    }


class QuestionsListView(View):
    def get(self, request):
        form = QuestionsForm()
        questions_list = Questions.objects.all()
        return render(request, "admin_panel/questions_list.html", {
            "form": form,
            "questions_list": questions_list,
            "title": "Список вопросов"
        })

    def post(self, request):
        form = QuestionsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            question = form.save()
            messages.success(request, "Вопрос успешно добавлен.")
            return redirect("questions_list")
        else:
            messages.error(request, "Ошибка добавления.")
            return redirect("questions_list")


class QuestionEditView(UpdateView):
    model = Questions
    form_class = QuestionsForm
    template_name = "admin_panel/question_edit.html"
    extra_context = {
        "title": "Изменить вопрос",
    }

    def get_queryset(self):
        return Questions.objects.filter(pk=self.kwargs.get("pk"))

    def get_success_url(self):
        messages.success(self.request, "Вопрос успешно обновлен.")
        return reverse_lazy("questions_list")
