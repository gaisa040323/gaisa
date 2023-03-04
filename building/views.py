from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.urls import reverse

from django.contrib.auth import login as auth_login

import datetime

import time

# Подключение моделей
from django.contrib.auth.models import User, Group

from django.db import models
from django.db.models import Q

from .models import Construction, Investor, Binding, Investments, Coming, Category, Catalog, Outgo, Sale, News
# Подключение форм
from .forms import InvestorForm, CategoryForm, NewsForm

from django.contrib.auth.models import AnonymousUser

# Create your views here.
# Групповые ограничения
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='403')

# Стартовая страница 
def index(request):
    news1 = News.objects.all().order_by('-daten')[0:1]
    news24 = News.objects.all().order_by('-daten')[1:4]
    return render(request, "index.html", {"news1": news1, "news24": news24 ,})    

# Контакты
def contact(request):
    return render(request, "contact.html")



# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def investor_index(request):
    #investor = Investor.objects.all().order_by('surname', 'name', 'patronymic')
    #return render(request, "investor/index.html", {"investor": investor})
    investor = Investor.objects.all().order_by('fio')
    return render(request, "investor/index.html", {"investor": investor})

# Список для просмотра
def investor_list(request):
    investor = Investor.objects.all().order_by('fio')
    return render(request, "investor/list.html", {"investor": investor})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def investor_create(request):
    if request.method == "POST":
        investor = Investor()        
        investor.fio = request.POST.get("fio")
        investor.email = request.POST.get("email")
        investor.phone = request.POST.get("phone")
        investor.link = request.POST.get("link")
        if 'photo' in request.FILES:                
            investor.photo = request.FILES['photo']        
        investor.save()
        return HttpResponseRedirect(reverse('investor_index'))
    else:        
        #investorform = InvestorForm(request.FILES, initial={'daten': datetime.datetime.now().strftime('%Y-%m-%d'),})
        investorform = InvestorForm()
        return render(request, "investor/create.html", {"form": investorform})

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
@login_required
@group_required("Managers")
def investor_edit(request, id):
    try:
        investor = Investor.objects.get(id=id) 
        if request.method == "POST":
            investor.fio = request.POST.get("fio")
            investor.email = request.POST.get("email")
            investor.phone = request.POST.get("phone")
            investor.link = request.POST.get("link")
            if "photo" in request.FILES:                
                investor.photo = request.FILES["photo"]
            investor.save()
            return HttpResponseRedirect(reverse('investor_index'))
        else:
            # Загрузка начальных данных
            investorform = InvestorForm(initial={'fio': investor.fio, 'email': investor.email, 'phone': investor.phone, 'link': investor.link, 'photo': investor.photo })
            return render(request, "investor/edit.html", {"form": investorform})
    except Investor.DoesNotExist:
        return HttpResponseNotFound("<h2>Investor not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def investor_delete(request, id):
    try:
        investor = Investor.objects.get(id=id)
        investor.delete()
        return HttpResponseRedirect(reverse('investor_index'))
    except Investor.DoesNotExist:
        return HttpResponseNotFound("<h2>Investor not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def investor_read(request, id):
    try:
        investor = Investor.objects.get(id=id) 
        return render(request, "investor/read.html", {"investor": investor})
    except Investor.DoesNotExist:
        return HttpResponseNotFound("<h2>Investor not found</h2>")


# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def category_index(request):
    category = Category.objects.all().order_by('title')
    return render(request, "category/index.html", {"category": category,})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def category_create(request):
    try:
        if request.method == "POST":
            category = Category()
            category.title = request.POST.get("title")
            categoryform = CategoryForm(request.POST)
            if categoryform.is_valid():
                category.save()
                return HttpResponseRedirect(reverse('category_index'))
            else:
                return render(request, "category/create.html", {"form": categoryform})
        else:        
            categoryform = CategoryForm()
            return render(request, "category/create.html", {"form": categoryform})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Category.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Category.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def category_edit(request, id):
    try:
        category = Category.objects.get(id=id)
        if request.method == "POST":
            category.title = request.POST.get("title")
            categoryform = CategoryForm(request.POST)
            if categoryform.is_valid():
                category.save()
                return HttpResponseRedirect(reverse('category_index'))
            else:
                return render(request, "category/edit.html", {"form": categoryform})
        else:
            # Загрузка начальных данных
            categoryform = CategoryForm(initial={'title': category.title, })
            return render(request, "category/edit.html", {"form": categoryform})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def category_delete(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return HttpResponseRedirect(reverse('category_index'))
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
def category_read(request, id):
    try:
        category = Category.objects.get(id=id) 
        return render(request, "category/read.html", {"category": category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)


# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def news_index(request):
    #news = News.objects.all().order_by('surname', 'name', 'patronymic')
    #return render(request, "news/index.html", {"news": news})
    news = News.objects.all().order_by('-daten')
    return render(request, "news/index.html", {"news": news})

# Список для просмотра
def news_list(request):
    news = News.objects.all().order_by('-daten')
    return render(request, "news/list.html", {"news": news})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def news_create(request):
    if request.method == "POST":
        news = News()        
        news.daten = request.POST.get("daten")
        news.title = request.POST.get("title")
        news.details = request.POST.get("details")
        if 'photo' in request.FILES:                
            news.photo = request.FILES['photo']        
        news.save()
        return HttpResponseRedirect(reverse('news_index'))
    else:        
        #newsform = NewsForm(request.FILES, initial={'daten': datetime.datetime.now().strftime('%Y-%m-%d'),})
        newsform = NewsForm(initial={'daten': datetime.datetime.now().strftime('%Y-%m-%d'), })
        return render(request, "news/create.html", {"form": newsform})

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
@login_required
@group_required("Managers")
def news_edit(request, id):
    try:
        news = News.objects.get(id=id) 
        if request.method == "POST":
            news.daten = request.POST.get("daten")
            news.title = request.POST.get("title")
            news.details = request.POST.get("details")
            if "photo" in request.FILES:                
                news.photo = request.FILES["photo"]
            news.save()
            return HttpResponseRedirect(reverse('news_index'))
        else:
            # Загрузка начальных данных
            newsform = NewsForm(initial={'daten': news.daten.strftime('%Y-%m-%d'), 'title': news.title, 'details': news.details, 'photo': news.photo })
            return render(request, "news/edit.html", {"form": newsform})
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def news_delete(request, id):
    try:
        news = News.objects.get(id=id)
        news.delete()
        return HttpResponseRedirect(reverse('news_index'))
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def news_read(request, id):
    try:
        news = News.objects.get(id=id) 
        return render(request, "news/read.html", {"news": news})
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Регистрационная форма 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
            #return render(request, 'registration/register_done.html', {'new_user': user})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# Изменение данных пользователя
@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('index')
    #success_url = reverse_lazy('my_account')
    def get_object(self):
        return self.request.user



