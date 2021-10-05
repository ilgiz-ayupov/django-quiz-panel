from django.db import models
from django.contrib.auth.models import User


class TelegramUser(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    username = models.CharField(max_length=255, verbose_name="Имя пользователя")
    telegram_id = models.IntegerField(verbose_name="Telegram ID")
    true_answer = models.PositiveIntegerField(verbose_name="Правильных ответов", null=True)
    false_answer = models.PositiveIntegerField(verbose_name="Неправильных ответов", null=True)
    current_question = models.PositiveIntegerField(verbose_name="Текущий вопрос", null=True)

    def __str__(self):
        return f"{self.first_name} - {self.telegram_id}"

    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"


class Questions(models.Model):
    title = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.CharField(max_length=255, verbose_name="Ответ")
    image = models.ImageField(upload_to="question_photos/", verbose_name="Картинка", null=True, blank=True)
    answer_option_one = models.CharField(max_length=255, verbose_name="Вариант ответа 1")
    answer_option_two = models.CharField(max_length=255, verbose_name="Вариант ответа 2")
    answer_option_third = models.CharField(max_length=255, verbose_name="Вариант ответа 3")
    answer_option_four = models.CharField(max_length=255, verbose_name="Вариант ответа 4")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
