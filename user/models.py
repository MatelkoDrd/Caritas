from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    password2 = models.CharField(max_length=32)
    NAME_FIELD = 'email'
