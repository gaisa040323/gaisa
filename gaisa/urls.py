"""gaisa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static

from building import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('i18n/', include('django.conf.urls.i18n')),

    path('investor/index/', views.investor_index, name='investor_index'),
    path('investor/list/', views.investor_list, name='investor_list'),
    path('investor/create/', views.investor_create, name='investor_create'),
    path('investor/edit/<int:id>/', views.investor_edit, name='investor_edit'),
    path('investor/delete/<int:id>/', views.investor_delete, name='investor_delete'),
    path('investor/read/<int:id>/', views.investor_read, name='investor_read'),

    path('category/index/', views.category_index, name='category_index'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', views.category_delete, name='category_delete'),
    path('category/read/<int:id>/', views.category_read, name='category_read'),

    #path('coming/index/', views.coming_index, name='coming_index'),
    #path('coming/create/', views.coming_create, name='coming_create'),
    #path('coming/edit/<int:id>/', views.coming_edit, name='coming_edit'),
    #path('coming/delete/<int:id>/', views.coming_delete, name='coming_delete'),
    #path('coming/read/<int:id>/', views.coming_read, name='coming_read'),

    #path('catalog/index/<int:coming_id>/', views.catalog_index, name='catalog_index'),
    #path('catalog/list/', views.catalog_list, name='catalog_list'),
    #path('catalog/create/<int:coming_id>/', views.catalog_create, name='catalog_create'),
    #path('catalog/edit/<int:id>/<int:coming_id>/', views.catalog_edit, name='catalog_edit'),
    #path('catalog/delete/<int:id>/<int:coming_id>/', views.catalog_delete, name='catalog_delete'),
    #path('catalog/read/<int:id>/<int:coming_id>/', views.catalog_read, name='catalog_read'),
    #path('catalog/details/<int:id>/', views.catalog_details, name='catalog_details'),    
    #path('catalog/basket/', views.basket, name='basket'),
    #path('catalog/buy/', views.buy, name='buy'),

    path('news/index/', views.news_index, name='news_index'),
    path('news/list/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/edit/<int:id>/', views.news_edit, name='news_edit'),
    path('news/delete/<int:id>/', views.news_delete, name='news_delete'),
    path('news/read/<int:id>/', views.news_read, name='news_read'),

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
