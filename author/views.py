import datetime

from rest_framework import generics

from general.permissions import IsAdminOrReadOnly
from general.filters import person_view_filters
from .models import Author
from .serializers import AuthorSerializer


class AuthorView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = person_view_filters(self.request.query_params, Author)

        return queryset


class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
