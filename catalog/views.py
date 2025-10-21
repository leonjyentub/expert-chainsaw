from django.shortcuts import render
from django.http import HttpResponse

from .models import Book

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book_list.html', {'books': books})

def book(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book.html', {'book': book})