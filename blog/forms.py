from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, EmailMultiAlternatives
from PIL import Image

from django import forms
from .models import Profil


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput())
    body = forms.CharField(label='Сообщение', widget=forms.Textarea())


#PROFILE
class EditProfile(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['name', 'text', 'image']


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
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'placeholder': 'Имя',
    }))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'placeholder': 'Фамилия',
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


