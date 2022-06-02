from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "title", "author", "description", "created_at")
        model = Book


