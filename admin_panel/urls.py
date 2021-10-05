from django.urls import path

from .views import UsersListView, QuestionsListView, QuestionEditView

urlpatterns = [
    path("", UsersListView.as_view(), name="users_list"),
    path("question_list/", QuestionsListView.as_view(), name="questions_list"),
    path("question_edit/<int:pk>", QuestionEditView.as_view(), name="question_edit")
]
