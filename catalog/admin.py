from django.contrib import admin
from .models import Book, BorrowRecord

# id: user
# password: Test1234
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('published_date',)

#admin.site.register(Book, BookAdmin)

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('user__username', 'book__title')