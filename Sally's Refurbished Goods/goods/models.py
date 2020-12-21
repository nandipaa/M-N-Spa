from django.db import models


class Clothes(models.Model):
    name = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)
    price = models.FloatField()


class Household(models.Model):
    pass


class Eggs(models.Model):
    pass


