# from msilib.schema import ListView

from django.shortcuts import render, HttpResponse
from django.views import View
from Book.models import Book
from rest_framework import generics
from django.contrib.auth.models import User

from Book.serializer import BookSerializer


class BookView(generics.GenericAPIView):
    serializer_class = BookSerializer



