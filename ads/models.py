from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=49, verbose_name='Наименование')
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
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
