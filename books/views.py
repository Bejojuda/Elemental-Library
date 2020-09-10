from rest_framework import generics
from distutils.util import strtobool

from .models import Book, BookUnit
from .serializers import BookSerializer, BookUnitSerializer, BookAddUnitSerializer
from .filters import books_view_filters
from general.permissions import IsAdminOrReadOnly
from general.pagination import StandardResultsSetPagination, LargeResultsSetPagination


class BookView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = books_view_filters(self.request.query_params)

        return queryset


class BookDetailView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BookAddUnitSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        # Overwriting the creation so that, instead of adding a new Book, a new BookUnit is created
        validated_data = {}
        if 'serial' in serializer.data:
            validated_data['serial'] = serializer.data['serial']

        validated_data['book'] = self.queryset.get(pk=self.kwargs['pk'])
        book_unit = BookUnitSerializer.create(BookUnitSerializer, validated_data)
        return book_unit


class BookUnitView(generics.ListAPIView):
    serializer_class = BookUnitSerializer
    queryset = BookUnit.objects.all()
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        queryset = BookUnit.objects.all()
        serial = self.request.query_params.get('serial', None)
        borrowed = self.request.query_params.get('borrowed', None)

        if serial:
            queryset = BookUnit.objects.filter(serial__iexact=serial)
        if borrowed:
            try:
                borrowed = strtobool(borrowed)

                queryset = BookUnit.objects.filter(borrowed=borrowed)
            except ValueError:
                print("Error")

        return queryset


class BookUnitDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BookUnitSerializer

    # Narrows down the BookUnits that belong to the specified Book
    # And then gets the specific BookUnit by the pk
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        book_id = self.kwargs.get('book_id')
        return BookUnit.objects.filter(pk=pk, book__pk=book_id)





