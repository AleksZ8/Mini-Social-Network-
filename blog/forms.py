from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from PIL import Image

from django import forms
from .models import Profil


class Myprofile(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['name', 'text', 'image']

#RLL
class AuthUser(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login',
    }))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))


class UserRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


