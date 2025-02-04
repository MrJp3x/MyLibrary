from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1
        # read_only_fields = ('created_at', 'updated_at')
        # write_only_fields = ('created_at', 'updated_at')

