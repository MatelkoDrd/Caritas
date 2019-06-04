from django.db import models
from organization.models import Organization
# Create your models here.


TYPE_CHOICES = (
    (1, "Adult"),
    (2, "Kid")
)


SEX_CHOICES = (
    (1, "Male"),
    (2, "Female"),
)

SIZE_CHOICES = (
    (1, "S"),
    (2, "M"),
    (3, "L"),
)


class Clothes(models.Model):

    type = models.IntegerField(choices=TYPE_CHOICES)
    size = models.IntegerField(choices=SIZE_CHOICES)
    sex = models.IntegerField(choices=SEX_CHOICES)
    quantity = models.IntegerField()


class Toy(models.Model):

    name = models.CharField(max_length=64)
    quantity = models.IntegerField()


class Book(models.Model):

    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    type = models.IntegerField(choices=TYPE_CHOICES)
    quantity = models.IntegerField()


class Other(models.Model):

    type = models.IntegerField(choices=TYPE_CHOICES)
    sex = models.IntegerField(choices=SEX_CHOICES)
    quantity = models.IntegerField()


class Location(models.Model):

    street = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=64)
    city = models.CharField(max_length=64)


class Giveaway(models.Model):

    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    others = models.ForeignKey(Other, on_delete=models.CASCADE)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    bags = models.IntegerField()
