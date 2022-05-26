from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),


    path('register/', views.register, name='register'),
    path('verify_email/<uidb64>/<token>/',views.EmailVerify.as_view(),name='verify_email'),
    path('auth/', views.authentication, name='auth'),
    path('quit/', views.quit, name='quit'),
    path('change/', views.changepassword, name='change_password'),

    path('add_page/', views.add_page, name='add_page'),
    path('pages/', views.All_Pages.as_view(), name='pages'),
    path('profile/', views.my_profile, name='profil'),
    path('profile/<int:profile_id>', views.edit_profile, name='editprofil'),
    path('send_message/<int:user_id>', views.send_mes, name='send'),
    path('delprofile/<int:profile_id>', views.delprofile, name='delprofile'),
    path('page/<int:id>/', views.profileview, name='detail'),
    path('test/', views.test_view, name='test'),
]
