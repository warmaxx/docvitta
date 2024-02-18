from django.shortcuts import render, get_object_or_404
from homepage.models import Departament, Employee, Vacancy, Page, Article, Sale


# Create your views here.
def index(request):
    departaments = Departament.objects.all()
    context = {
        'departaments': departaments,
    }
    return render(request, 'homepage/index.html', context=context)


def about(request):
    context = {}
    return render(request, 'homepage/about-us.html', context=context)


def contact(request):
    context = {}
    return render(request, 'homepage/contact.html', context=context)


def services(request):
    context = {}
    return render(request, 'homepage/services.html', context=context)


def doctors(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'homepage/doctors.html', context=context)


def doctor(request, id):
    doctor = get_object_or_404(Employee, id=id)
    employees = Employee.objects.all().exclude(id=id)
    context = {
        'doctor': doctor,
        'employees': employees,
    }
    return render(request, 'homepage/doctor.html', context=context)


def vacancy(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies, }
    return render(request, 'homepage/vacancy.html', context=context)


def vacancy_info(request, id):
    vacancy = get_object_or_404(Vacancy, pk=id)
    vacancies = Vacancy.objects.all().exclude(id=id)
    context = {'vacancy': vacancy,
               'vacancies': vacancies,
               }
    return render(request, 'homepage/vacancy_info.html', context=context)


def page(request, id):
    page = get_object_or_404(Page, pk=id)
    pages = Page.objects.all().exclude(id=id)
    context = {'page': page, 'pages': pages, }
    return render(request, 'homepage/page.html', context=context)


def rules(request):
    context = {}
    return render(request, 'homepage/rules.html', context=context)


def articles(request):
    articles = Article.objects.all()
    pages = Page.objects.all()
    context = {'articles': articles, 'pages': pages}
    return render(request, 'homepage/articles.html', context=context)


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    articles = Article.objects.all().exclude(id=id)
    context = {'article': article, 'articles': articles}
    return render(request, 'homepage/article.html', context=context)


def sales(request):
    sales = Sale.objects.all()
    context = {
        'sales': sales,
    }
    return render(request, 'homepage/sales.html', context=context)


def sale(request, id):
    sale = get_object_or_404(Sale, id=id)
    sales = Sale.objects.all().exclude(id=id)
    context = {
        'sale': sale,
        'sales':sales,
    }
    return render(request, 'homepage/sale.html', context=context)
