"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from catalog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # Home page redirects to urls 'catalog/'
    path('', views.book_list, name='home'),
    path('catalog/', views.index, name='index'),
    path('catalog/books/', views.book_list, name='book_list'),
    path('catalog/books/<int:pk>/', views.book, name='book_detail'),
    path('catalog/books/add/', views.add_book, name='add_book'),
    path('catalog/books/add2/', views.add_book_model_form, name='add_book_model_form'),
    path('accounts/', include('accounts.urls')),
    path('catalog/book_search/', views.book_search, name='book_search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
