from django import forms  # required package for form
from .models import News  # required News package for make form for news site
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):  # creation form
    def __init__(self, *args, **kwargs):  # preparation for making normal field
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'  # Making normal field instead '-----'

    class Meta:  # creating beautiful view for form
        model = News
        fields = ['title', 'content', 'is_published', 'photo', 'category']
        widgets = {'title': forms.TextInput(attrs={"class": "form-control"}),
                   'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
                   'is_published': forms.CheckboxInput(attrs={"class": "form-check-input"}),
                   'category': forms.Select(attrs={"class": "form-control"})
                   }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\W', title):
            raise ValidationError('Название не должно начинаться с спецсимвола!')
        return title


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Имя пользователя должно состоять из букв, цифр и символов.',
                               widget=forms.TextInput(
                                   attrs={"class": "form-control", 'autocomplete': 'off'}))
    email = forms.EmailField(
        label='Электронная почта', help_text='mail@mail.com', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label='Пароль',help_text='Пароль должен быть не короче 8 символов.',
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        label='Подтверждение пароля', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Neta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Введите ваш логин.',
                               widget=forms.TextInput(
                                   attrs={"class": "form-control", 'autocomplete': 'off'}))
    password = forms.CharField(
        label='Пароль', help_text='Введите пароль.',
        widget=forms.PasswordInput(attrs={"class": "form-control"}))

