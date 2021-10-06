from django.db import models


class TelegramUser(models.Model):
    STATUS_LOGGED = "Авторизовался"
    STATUS_ACTIVE = "Проходит викторину"
    STATUS_END = "Закончил викторину"

    STATUS_CHOICES = [
        (STATUS_LOGGED, "Авторизовался"),
        (STATUS_ACTIVE, "Проходит викторину"),
        (STATUS_END, "Закончил викторину")
    ]

    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    username = models.CharField(max_length=255, verbose_name="Имя пользователя")
    telegram_id = models.IntegerField(verbose_name="Telegram ID")
    true_answer = models.PositiveIntegerField(verbose_name="Правильных ответов", null=True)
    false_answer = models.PositiveIntegerField(verbose_name="Неправильных ответов", null=True)
    current_question = models.PositiveIntegerField(verbose_name="Текущий вопрос", null=True)
    status = models.CharField(max_length=255, verbose_name="Статус", choices=STATUS_CHOICES, default=STATUS_LOGGED)
    start_game = models.DateTimeField(auto_now_add=True, verbose_name="Начало викторины", null=True)
    duration_game = models.CharField(max_length=255, verbose_name="Продолжительтельность игры", null=True)

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
