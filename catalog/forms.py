# 建立跟models.py的Book相關的form
from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label="書名", max_length=200)
    author = forms.CharField(label="作者", max_length=100)
    published_date = forms.DateField(label="出版日期")
    isbn = forms.CharField(label="ISBN", max_length=13)