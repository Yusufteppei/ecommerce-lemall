from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=32)
    salary = models.IntegerField()


class Staff(models.Model):
    position = models.ManyToManyField(Position)
    full_name = models.CharField(max_length=64)
    #   phone = models.PhoneNumberField()
    #   address = models.AddressField()
    #   salary = models.IntegerField()

# MODELS INHERITANCE DJANGO???????