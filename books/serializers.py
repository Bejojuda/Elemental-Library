from rest_framework import serializers

from .models import Book, BookUnit


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        fields = '__all__'


class BookUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookUnit

        fields = '__all__'