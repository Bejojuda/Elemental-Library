from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User

from .models import Person
from .serializers import PersonSerializer
from .permissions import IsSelfOrReadOnly


class PersonView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = User.objects.all()

    # def perform_create(self, serializer):
    #    return Person.objects.create_user(**serializer.validated_data)


class PersonDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSelfOrReadOnly]
    serializer_class = PersonSerializer
    queryset = User.objects.all()

