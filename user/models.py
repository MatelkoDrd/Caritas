from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):

    user_data = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=64)
    age = models.IntegerField()


    def __str__(self):
        return self.user_data.email

