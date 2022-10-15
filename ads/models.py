from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=5000, null=True)
    address = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name