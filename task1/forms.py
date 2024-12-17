from django import forms
from django.core.exceptions import ValidationError
from .models import Buyer


class UserRegister(forms.Form):

    username = forms.CharField(max_length=30, label='Введите логин: ',
                               error_messages={'required': 'Повторите попытку.'})

    password = forms.CharField(min_length=8, label=' Введите пароль: ',
                               error_messages={'required': 'Повторите попытку.'},
                               widget=forms.PasswordInput())

    repeat_password = forms.CharField(min_length=8, label=' Повторите пароль ',
                                      error_messages={'required': 'Повторите попытку.'},
                                      widget=forms.PasswordInput())

    age = forms.IntegerField(min_value=18, label='Введите свой возраст',
                             error_messages={'required': 'Вы должны быть старше 18.', })


    def clean_username(self):
        data = self.cleaned_data["username"]
        # Получаем всех пользователей
        users = Buyer.objects.values_list('username', flat=True)
        if data in users:
            raise ValidationError(f"Пользователь {data} уже зарегистрирован.")

        return data

