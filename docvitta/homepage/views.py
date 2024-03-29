from django.shortcuts import render, get_object_or_404, redirect

from docvitta import settings
from homepage.models import Departament, Employee, Vacancy, Page, Article, Sale, Partner
from django.template.loader import render_to_string
from django.core.mail import send_mail
import datetime


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
    date = datetime.date.today()
    sales = Sale.objects.filter(date_start__lte=date).filter(date_end__gte=date).filter(active=True).order_by('-id')
    context = {
        'sales': sales,
    }
    return render(request, 'homepage/sales.html', context=context)


def sale(request, id):
    sale = get_object_or_404(Sale, id=id)
    date = datetime.date.today()
    if (sale.date_start > date) or (sale.date_end <= date) or (sale.active == False):
        return redirect('homepage:sales')
    sales = Sale.objects.all().exclude(id=id)
    context = {
        'sale': sale,
        'sales': sales,
    }
    return render(request, 'homepage/sale.html', context=context)


def partners(request):
    partners = Partner.objects.all()
    context = {
        'partners': partners,
    }
    return render(request, 'homepage/partners.html', context=context)


def form_anketa(request):
    if request.method == 'GET':
        return render(request, 'homepage/form_anketa.html')
    post = request.POST
    answers = []
    for k, v in post.items():
        if k != 'csrfmiddlewaretoken':
            answers.append(v)
    # print(answers)
    email_title = 'Анкета посетителя с сайта docvitta.ru'
    msg_html = render_to_string('homepage/email_anketa.html', {'answers': answers})
    send_mail(
        email_title,
        msg_html,
        settings.DEFAULT_FROM_EMAIL,
        [
            'info@docvitta.ru',
            # 'Maksyagin.Aleksey@vitta.ru',
        ],
        html_message=msg_html,
    )
    return render(request, 'homepage/form_anketa_send.html')
