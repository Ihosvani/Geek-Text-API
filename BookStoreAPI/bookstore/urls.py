"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from books import views

urlpatterns = [
    path('', views.welcomePage),
    path('books/', views.getBooks),
    path('admin/books/', views.createBook),
    path('books/<int:ISBN>', views.bookISBN ),
    path('books/mostSold',views.getTopTenBooks),
    path('books/genre/<str:genre>', views.getBookGenre),
    path('authors/', views.getAuthors),
    path('admin/authors/', views.createAuthor),
    path('authors/<str:author>', views.booksByAuthor),
    path('books/rateBook', views.rateBook),
    path('books/commentBook', views.commentBook)
]
