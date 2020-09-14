from rest_framework import generics
from django_filters import rest_framework as filters

from django.contrib.auth.models import User

from .filters import person_view_ordering, PersonFilter
from .serializers import PersonSerializer
from .permissions import IsSelfOrReadOnly
from general.pagination import StandardResultsSetPagination


class PersonView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PersonFilter

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = person_view_ordering(self.request.query_params, queryset)

        return queryset


class PersonDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSelfOrReadOnly]
    serializer_class = PersonSerializer
    queryset = User.objects.all()

