from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

# Create your models here.
class Departament(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название отделения')
    description = models.TextField(verbose_name='Описание')
    icon = models.ImageField(upload_to='images/icons/', verbose_name='Иконка отделения')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='Отделение', null=True,
                                    blank=True)
    photo = models.ImageField(upload_to='images/photos/', verbose_name='Фото', null=True, blank=True)
    job = models.CharField(max_length=100, verbose_name='Должность', default='')
    info = RichTextField(verbose_name='Информация об образовании и аккредитации', default='')

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок страницы')
    image = models.ImageField(upload_to='images/pages/', verbose_name='Изображение', null=True, blank=True)
    text = RichTextField(verbose_name='Контент страницы')

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    image = models.ImageField(upload_to='images/pages/', verbose_name='Изображение', null=True, blank=True)
    text = RichTextField(verbose_name='Контент статьи')

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название вакансии')
    text = RichTextField(verbose_name='Описание вакансии')

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    text = RichTextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='images/sales/', verbose_name='Изображение', null=True, blank=True)
    file = models.FileField(upload_to='images/sales/', verbose_name='Описание акции', null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='Активность')
    date_start = models.DateField(blank=True, default=date.today())
    date_end = models.DateField(blank=True, default=date.today())
    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='images/partners/', verbose_name='Логотип', null=True, blank=True)
    url = models.URLField(verbose_name='Ссылка на партнера', null=True, blank=True)

    def __str__(self):
        return self.name
