from django.shortcuts import render
from django.http import HttpResponse

from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

# filter books by search query if provided
from datetime import datetime
def book_search(request):
    query = request.GET.get('q', '').strip()
    author = request.GET.get('author', '').strip()
    published_from = request.GET.get('published_from', '').strip()
    published_to = request.GET.get('published_to', '').strip()

    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query)
    if author:
        books = books.filter(author__icontains=author)

    if published_from:
        try:
            df = datetime.strptime(published_from, '%Y-%m-%d').date()
            books = books.filter(published_date__gte=df)
        except ValueError:
            # 非法日期，忽略該條件
            pass

    if published_to:
        try:
            dt = datetime.strptime(published_to, '%Y-%m-%d').date()
            books = books.filter(published_date__lte=dt)
        except ValueError:
            pass

    books = books.order_by('-published_date')
    return render(request, 'book_list.html', 
                  {
                      'books': books, 
                      'query': query, 
                      'author': author,
                      'published_from': published_from,
                      'published_to': published_to
                  })

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
            #return HttpResponse("Book added successfully!")
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def add_book_model_form(request):
    from .forms import BookModelForm
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("Book added successfully using ModelForm!")
    else:
        form = BookModelForm()
    return render(request, 'add_book.html', {'form': form})