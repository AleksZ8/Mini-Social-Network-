from django.test import TestCase, Client

from django.contrib.auth import get_user_model

from blog.models import Profil, Comment

User = get_user_model()


class ModelTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='Aleks',
                            password='qwerty12345aa',
                            email='aleks.zurnachyan@bk.ru',
                            status=True,
                            is_active=True)
        Profil.objects.create(profil=User.objects.get(pk=1),
                              name='Alex',
                              text='test',
                              image=f'media/users/2022-05-22_21.56.47.jpg',
                              ip='127.0.0.1',
                              city='Armenia')

    def test_Profile_create(self):
        """Проверка на создание обьектов в БД"""
        prof = Profil.objects.get(pk=1)
        self.assertEqual(prof.name, 'Alex')
