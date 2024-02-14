from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Employee, Vacancy, Page, Article


class StaticSitemap(Sitemap):
    def items(self):
        # возвращайте объекты, которые вы хотите включить в карту сайта
        return ['homepage:index', 'homepage:about', 'homepage:contact', 'homepage:doctors', 'homepage:vacancy',
                'homepage:articles', 'homepage:rules']

    def location(self, item):
        # возвращает URL-адрес для каждого объекта
        return reverse(item)

    def priority(self, item):
        return 0.5  # Задайте приоритет для страницы врача

    def changefreq(self, item):
        return 'daily'  # Задайте частоту изменений для страницы


class DoctorSitemap(Sitemap):
    def items(self):
        return Employee.objects.all()

    def location(self, item):
        return reverse('homepage:doctor', args=[item.id])

    def priority(self, item):
        return 0.5  # Задайте приоритет для страницы врача

    def changefreq(self, item):
        return 'daily'  # Задайте частоту изменений для страницы


class VacancySitemap(Sitemap):
    def items(self):
        return Vacancy.objects.all()

    def location(self, item):
        return reverse('homepage:vacancy_info', args=[item.id])

    def priority(self, item):
        return 0.5  # Задайте приоритет для страницы врача

    def changefreq(self, item):
        return 'daily'  # Задайте частоту изменений для страницы


class PageSitemap(Sitemap):
    def items(self):
        return Page.objects.all()

    def location(self, item):
        return reverse('homepage:page', args=[item.id])

    def priority(self, item):
        return 0.5  # Задайте приоритет для страницы врача

    def changefreq(self, item):
        return 'daily'  # Задайте частоту изменений для страницы


class ArticleSitemap(Sitemap):
    def items(self):
        return Article.objects.all()

    def location(self, item):
        return reverse('homepage:article', args=[item.id])

    def priority(self, item):
        return 0.5  # Задайте приоритет для страницы врача

    def changefreq(self, item):
        return 'daily'  # Задайте частоту изменений для страницы
