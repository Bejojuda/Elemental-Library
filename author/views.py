from rest_framework import generics

from general.permissions import IsAdminOrReadOnly
from .models import Author
from .serializers import AuthorSerializer


class AuthorView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()