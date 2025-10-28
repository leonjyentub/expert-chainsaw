from django.shortcuts import render
from django.http import HttpResponse

from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book_list.html', {'books': books})

def book(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = Book(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                published_date=form.cleaned_data['published_date'],
                isbn=form.cleaned_data['isbn']
            )
            new_book.save()
            return HttpResponse("Book added successfully!")
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})