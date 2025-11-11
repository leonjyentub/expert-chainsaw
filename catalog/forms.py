# 建立跟models.py的Book相關的form
from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label="書名", max_length=200)
    author = forms.CharField(label="作者", max_length=100)
    published_date = forms.DateField(label="出版日期")
    isbn = forms.CharField(label="ISBN", max_length=13)

# 跟上面一樣的form，但用ModelForm來建立
from .models import Book
class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
        labels = {
            'title': '書名',
            'author': '作者',
            'published_date': '出版日期',
            'isbn': 'ISBN',
        }
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
        