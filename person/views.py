import datetime

from django.db.models.functions import Lower
from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User

from .filters import person_view_filters, person_view_ordering
from .serializers import PersonSerializer
from .permissions import IsSelfOrReadOnly
from general.pagination import StandardResultsSetPagination


class PersonView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = person_view_filters(self.request.query_params)
        queryset = person_view_ordering(self.request.query_params, queryset)

        return queryset


class PersonDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSelfOrReadOnly]
    serializer_class = PersonSerializer
    queryset = User.objects.all()

