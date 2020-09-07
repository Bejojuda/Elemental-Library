from django.db import models
from rest_framework import serializers
from django.utils.crypto import get_random_string

from .models import Book, BookUnit


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        fields = '__all__'



class BookUnitSerializer(serializers.ModelSerializer):

    serial = serializers.CharField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BookUnit

        fields = ['serial', 'book']

    def create(self, validated_data):
        print(validated_data)
        validated_data['serial'] = get_random_string(length=16)

        book_unit = BookUnit.objects.create(**validated_data)
        return book_unit


class BookAddUnitSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(read_only=True)
    #description = serializers.CharField(read_only=True)
    # author = serializers.CharField(source='book__author.name')
    book_units = BookUnitSerializer(many=True, read_only=True)
    serial = serializers.CharField(min_length=16, max_length=16, required=False)

    class Meta:
        model = Book

        fields = '__all__'

    # Modify fields propoerties depending on the HTTP Method
    def get_fields(self, *args, **kwargs):
        fields = super(BookAddUnitSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        # if the method is POST, make name, description and author read_ony
        if request and getattr(request, 'method', None) == "POST":
            fields['name'].read_only = True
            fields['description'].read_only = True
            # fields['author'].read_only = True
        if request and getattr(request, 'method', None) == "PUT":
            fields['serial'].read_only = True
        return fields
