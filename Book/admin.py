from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publisher')


    # list_filter = ('publisher', 'author')
    # search_fields = ('title', 'author')
    # prepopulated_fields = {'slug': ('title',)}
    # date_hierarchy = 'publisher'
    # ordering = ('publisher', 'title')
    # empty_value_display = '-empty-'
    # def save_model(self, request, obj, form, change):
    #     obj.author = request.user
    #     obj.publisher = request.user
    #     obj.save()
    #     super(BookAdmin, self).save_model(request, obj, form, change)
    #

admin.site.register(Book, BookAdmin)
