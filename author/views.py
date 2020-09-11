import datetime

from rest_framework import generics

from general.permissions import IsAdminOrReadOnly
from general.pagination import SmallResultsSetPagination
from .filters import authors_view_filters, authors_view_ordering
from .models import Author
from .serializers import AuthorSerializer


class AuthorView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AuthorSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        queryset = authors_view_filters(self.request.query_params)
        queryset = authors_view_ordering(self.request.query_params, queryset)

        return queryset


class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
