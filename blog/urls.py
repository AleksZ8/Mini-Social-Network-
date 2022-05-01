from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_page/', add_page, name='add_page'),
    path('pages/', all_pages.as_view(), name='pages'),
    path('profile/', my_profile, name='profil'),
    path('profile/<int:profile_id>', edit_profile, name='editprofil'),
    path('send_message/<int:user_id>', send_mes, name='send'),
    path('delprofile/<int:profile_id>', delprofile, name='delprofile'),
    path('change/', change, name='change'),
]
