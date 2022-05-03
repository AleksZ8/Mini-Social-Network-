from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    #reg
    path('register/', register, name='register'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('auth/', authentication, name='auth'),
    path('quit/', quit, name='quit'),
    path('change/', changepassword, name='change_password'),
    #profil
    path('add_page/', add_page, name='add_page'),
    path('pages/', All_Pages.as_view(), name='pages'),
    path('profile/', my_profile, name='profil'),
    path('profile/<int:profile_id>', edit_profile, name='editprofil'),
    path('send_message/<int:user_id>', send_mes, name='send'),
    path('delprofile/<int:profile_id>', delprofile, name='delprofile'),
    path('page/<int:id>/', profileview, name='detail'),
]
