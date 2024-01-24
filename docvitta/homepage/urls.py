from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('vacancy/<int:id>/', views.vacancy_info, name='vacancy_info'),
    path('article/', views.articles, name='articles'),
    path('article/<int:id>/', views.article, name='article'),
    path('page/<int:id>/', views.page, name='page'),
    path('rules/', views.rules, name='rules'),
]