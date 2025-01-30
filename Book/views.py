# from msilib.schema import ListView
from django.shortcuts import render, HttpResponse
from django.views import View
from Book.models import Book


class BookListView(View):
    model = Book
    def get(self, request):
        return HttpResponse('Book List')


