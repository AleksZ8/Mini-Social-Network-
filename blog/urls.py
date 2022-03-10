from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('auth/', authentication, name='auth'),
    path('quit/', quit, name='quit'),
    path('add_page/', add_page, name='add_page'),
    path('pages/', All_Pages.as_view(), name='pages'),
    path('profile/', my_profile, name='profil'),
    path('profile/<int:profile_id>', edit_profile, name='editprofil'),
]