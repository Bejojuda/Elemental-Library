from rest_framework import generics

from .models import Book, BookUnit
from .serializers import BookSerializer, BookUnitSerializer, BookAddUnitSerializer


class BookView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    serializer_class = BookAddUnitSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        validated_data = {}
        validated_data['book'] = self.queryset.get(pk=self.kwargs['pk'])
        print(validated_data)
        return BookUnitSerializer.create(BookUnitSerializer, validated_data)


class BookUnitView(generics.ListCreateAPIView):
    serializer_class = BookUnitSerializer
    queryset = BookUnit.objects.all()


