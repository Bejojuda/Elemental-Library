from rest_framework import generics
from django_filters import rest_framework as filters

from django.contrib.auth.models import User

from .filters import person_view_ordering, PersonFilter
from .serializers import PersonSerializer
from .permissions import IsSelfOrReadOnly
from general.pagination import StandardResultsSetPagination, LargeResultsSetPagination


class PersonView(generics.ListCreateAPIView):
    """
    List and Create all of the created People
    """
    serializer_class = PersonSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PersonFilter

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = person_view_ordering(self.request.query_params, queryset)

        return queryset


class PersonDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, Update and Delete a specific Person
    """
    permission_classes = [IsSelfOrReadOnly]
    serializer_class = PersonSerializer
    queryset = User.objects.all()

