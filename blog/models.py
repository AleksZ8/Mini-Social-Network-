from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    profil = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='users')

    def __str__(self):
        return self.name



