from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, DoctorSitemap, VacancySitemap, PageSitemap, ArticleSitemap

sitemaps = {
    'StaticSitemap': StaticSitemap,
    'DoctorSitemap': DoctorSitemap,
    'VacancySitemap': VacancySitemap,
    'PageSitemap': PageSitemap,
    'ArticleSitemap': ArticleSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/<int:id>/', views.doctor, name='doctor'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('vacancy/<int:id>/', views.vacancy_info, name='vacancy_info'),
    path('article/', views.articles, name='articles'),
    path('article/<int:id>/', views.article, name='article'),
    path('page/<int:id>/', views.page, name='page'),
    path('rules/', views.rules, name='rules'),
    path('sales/', views.sales, name='sales'),
    path('sales/<int:id>/', views.sale, name='sale'),
    path('partners/', views.partners, name='partners'),
    path('form_anketa/', views.form_anketa, name='form_anketa'),
]
