from django.db import models

# Create your models here.

TYPE_CHOICES = (

    (1, "Foundation"),
    (2, "Partners"),
    (3, "Locals")
)


class Organization(models.Model):
    type = models.IntegerField(choices=TYPE_CHOICES)
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    location = models.CharField(max_length=128)
    description = models.TextField()