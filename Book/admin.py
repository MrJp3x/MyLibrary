from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publisher')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
