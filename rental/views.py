from rest_framework import generics

from .serializers import RentalSerializer, RentalReturnSerializer
from .models import Rental
from .filters import rentals_view_filters

from books.models import BookUnit


class RentalView(generics.ListAPIView):
    serializer_class = RentalSerializer

    def get_queryset(self):
        queryset = rentals_view_filters(self.request.query_params)

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
