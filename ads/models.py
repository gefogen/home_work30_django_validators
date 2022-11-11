from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(null=True, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(10)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=49, verbose_name='Наименование', validators=[MinLengthValidator(10)])
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(max_length=5000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-price']

    def __str__(self):
        return self.name


class Selection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name