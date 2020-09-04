from rest_framework import generics

from .models import Book, BookUnit
from .serializers import BookSerializer, BookUnitSerializer


class BookView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

