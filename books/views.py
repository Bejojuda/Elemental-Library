from rest_framework import generics

from .models import Book, BookUnit
from .serializers import BookSerializer, BookUnitSerializer, BookAddUnitSerializer
from general.permissions import IsAdminOrReadOnly


class BookView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


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


class BookUnitDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BookUnitSerializer

    # Narrows down the BookUnits that belong to the specified Book
    # And then gets the specific BookUnit by the pk
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        book_id = self.kwargs.get('book_id')
        return BookUnit.objects.filter(pk=pk, book__pk=book_id)





