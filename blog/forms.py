from blog.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from django import forms
from .models import Profil, Comment
from .tasks import send_activation_notification


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('profil', 'author')


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput())
    body = forms.CharField(label='Сообщение', widget=forms.Textarea())


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['name', 'text', 'image']


class Myprofile(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['name', 'text', 'image']


class AuthUser(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login',
    }))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            elif not self.user_cache.status:
                send_activation_notification.delay(self.user_cache)
                raise ValidationError('Нет подтвержден Email')
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'placeholder': 'Имя',
    }))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'placeholder': 'Фамилия',
    }))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.status = False
        if commit:
            user.save()
            return user

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
