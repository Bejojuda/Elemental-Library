from django.db.models import Q
from rest_framework import generics

from .serializers import RentalSerializer
from .models import Rental


class RentalView(generics.ListCreateAPIView):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()


class RentalDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()
