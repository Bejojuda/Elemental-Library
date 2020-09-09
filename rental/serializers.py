import datetime

from django.utils.timezone import make_aware
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Rental
from books.models import BookUnit
from person.serializers import PersonSerializer
from person.models import Person


class RentalSerializer(serializers.ModelSerializer):

    return_date = serializers.DateTimeField(read_only=True)
    rental_date = serializers.DateTimeField(read_only=True)
    person_type = serializers.CharField(read_only=True)

    person = serializers.CharField(read_only=True)

    class Meta:

        model = Rental

        fields = '__all__'

    # Overwriting the create method to check if a BookUnit is borrowed and to add Person info
    def create(self, validated_data):
        # The current person is obtained from the request
        user = self.context.get('request', None).user
        person = Person.objects.get(user__username=user.username)

        # The current person and person type are assigned to the Rental attributes
        validated_data['person'] = person
        validated_data['person_type'] = person.type

        # Checks if the user has been borrowed, if it has, it raises a ValidationError
        if not validated_data['book_unit'].borrowed:
            rental = Rental.objects.create(**validated_data)
            return rental
        else:
            raise serializers.ValidationError("Book is currently borrowed")


# Serializer to use when a BookUnit is returned
class RentalReturnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental

        fields = []

    # When a PUT is made to the endpoint, the serializer updates the return_date to the current Date
    def update(self, instance, validated_data):

        # make_aware needed because native value datetime.now is not accepted by the model
        if instance.return_date is None:
            instance.return_date = make_aware(datetime.datetime.now())
            instance.save()

        return instance


