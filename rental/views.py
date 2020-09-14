from rest_framework import generics
from django_filters import rest_framework as filters

from .serializers import RentalSerializer, RentalReturnSerializer
from .models import Rental
from .filters import rentals_view_filters, rentals_view_ordering, RentalFilter

from general.pagination import LargeResultsSetPagination


class RentalView(generics.ListAPIView):
    serializer_class = RentalSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RentalFilter

    def get_queryset(self):
        queryset = Rental.objects.all()
        queryset = rentals_view_ordering(self.request.query_params, queryset)

        return queryset


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
