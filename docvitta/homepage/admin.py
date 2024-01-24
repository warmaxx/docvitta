from django.contrib import admin
from homepage.models import Departament, Employee, Page, Vacancy, Article


# Register your models here.

class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    empty_value_display = '-пусто-'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'departament', 'job', 'info')
    empty_value_display = '-пусто-'


class PageAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Departament, DepartamentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Vacancy, VacancyAdmin)
