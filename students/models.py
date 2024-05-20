import django
from django.db import models
from datetime import date
# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Students(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    preview = models.ImageField(upload_to='students/',
                                verbose_name='превью', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')

    date_create = models.DateTimeField(
        default=django.utils.timezone.now, verbose_name='дата создания')

    date_change = models.DateTimeField(
        default=django.utils.timezone.now, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.name} {self.pk} {self.description} {self.category} {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.pk} {self.name} {self.description}'


class Meta:
    verbose_name = 'студенты'
    verbose_name_plural = 'студенты'
    ordering = ('category',)
