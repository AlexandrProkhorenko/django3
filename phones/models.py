import datetime

from django.db import models


class Phone(models.Model):




    name = models.SlugField(max_length=500)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.TextField()
    lte_exists = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)



