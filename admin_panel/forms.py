from django import forms
from .models import Questions


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = (
            "title", "answer", "image", "answer_option_one", "answer_option_two", "answer_option_third", "answer_option_four"
        )
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "answer": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "answer_option_one": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "answer_option_two": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "answer_option_third": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "answer_option_four": forms.TextInput(attrs={
                "class": "form-control"
            }),

        }
