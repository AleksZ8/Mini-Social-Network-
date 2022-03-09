from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('auth/', authentication, name='auth'),
    path('quit/', quit, name='quit'),
    path('profile/', profile, name='user'),
]