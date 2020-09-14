from django.db.models.functions import Lower
from django_filters import rest_framework as filters

from books.models import Book, BookUnit


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['name', 'author']


class BookUnitFilter(filters.FilterSet):

    class Meta:
        model = BookUnit
        fields = ['serial', 'borrowed']


def books_view_ordering(params, queryset):
    ordering = params.get('ordering', None)
    if ordering:
        if ordering == 'name':
            queryset = queryset.order_by(Lower('name'))
        elif ordering == '-name':
            queryset = queryset.order_by(Lower('name').desc())
        elif ordering == 'description':
            queryset = queryset.order_by(Lower('description'))
        elif ordering == '-description':
            queryset = queryset.order_by(Lower('description').desc())

    return queryset


def book_units_view_ordering(params, queryset):
    ordering = params.get('ordering', None)
    if ordering:
        if ordering == 'name':
            queryset = queryset.order_by(Lower('book__name'))
        elif ordering == '-name':
            queryset = queryset.order_by(Lower('book__name').desc())
        elif ordering == 'description':
            queryset = queryset.order_by(Lower('book__description'))
        elif ordering == '-description':
            queryset = queryset.order_by(Lower('book__description').desc())

    return queryset
