from django.core.validators import MinLengthValidator
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ('admin', 'администратор'),
        ('member', 'пользователь'),
        ('moderator', 'модератор')
    ]

    first_name = models.CharField(max_length=100, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, null=True, verbose_name='Фамилия')
    username = models.CharField(max_length=20, unique=True, verbose_name='Никнейм')
    password = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    role = models.CharField(max_length=10, choices=ROLES, default='member', verbose_name='Роль')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
