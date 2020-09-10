import datetime

from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User

from .serializers import PersonSerializer
from .permissions import IsSelfOrReadOnly
from general.filters import person_view_filters


class PersonView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = person_view_filters(self.request.query_params, User)

        return queryset


class PersonDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSelfOrReadOnly]
    serializer_class = PersonSerializer
    queryset = User.objects.all()

