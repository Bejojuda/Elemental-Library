from rest_framework import generics
from django_filters import rest_framework as filters

from .serializers import RentalSerializer, RentalReturnSerializer
from .models import Rental
from .filters import rentals_view_ordering, RentalFilter

from general.pagination import LargeResultsSetPagination


class RentalView(generics.ListAPIView):
    """
    Lists all of the created Rentals
    """
    serializer_class = RentalSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RentalFilter

    def get_queryset(self):
        queryset = Rental.objects.all()
        queryset = rentals_view_ordering(self.request.query_params, queryset)

        return queryset


class RentalBorrowView(generics.CreateAPIView):
    """
    Creates a new Rental, it takes the serial number of the BookUnit to be borrowed and
    internally assigns the logged User info and the rental_date to the current date
    """
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()


class RentalReturnView(generics.UpdateAPIView):
    """
    'Returns' a BookUnit, setting its borrowed attribute to False and setting the return_date to the current date
    """
    serializer_class = RentalReturnSerializer
    queryset = Rental.objects.all()


class RentalDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, Update and Delete a specific Rental
    """
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()
