from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Rental
from books.models import BookUnit


class RentalSerializer(serializers.ModelSerializer):

    return_date = serializers.DateField(required=False)
    rental_date = serializers.DateField(required=False)

    class Meta:
        model = Rental

        fields = '__all__'

    # Overwriting the create method to check if a BookUnit has already been borrowed
    def create(self, validated_data):
        if not validated_data['book_unit'].borrowed:
            book_unit = BookUnit.objects.get(pk=validated_data['book_unit'].id)
            book_unit.borrowed = True
            book_unit.save()
            validated_data['book_unit'].borrowed = True

            rental = Rental.objects.create(**validated_data)
            return rental
        else:
            raise serializers.ValidationError("Book is currently borrowed")


