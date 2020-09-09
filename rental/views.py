from django.db.models import Q
from rest_framework import generics

from .serializers import RentalSerializer, RentalReturnSerializer
from .models import Rental


class RentalView(generics.ListAPIView):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()


# View used to create a book
class RentalBorrowView(generics.CreateAPIView):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()


# View to return a BookUnit (make return_date the current datetime)
class RentalReturnView(generics.UpdateAPIView):
    serializer_class = RentalReturnSerializer
    queryset = Rental.objects.all()


class RentalDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()
