import datetime
from django_filters import rest_framework as filters

from django.utils.timezone import make_aware

from .models import Rental


class RentalFilter(filters.FilterSet):
    book_name = filters.CharFilter(field_name="book_unit__book__name", lookup_expr='icontains')
    rental_date_gte = filters.DateTimeFilter(field_name="rental_date", lookup_expr='gte')
    rental_date_lte = filters.DateTimeFilter(field_name="rental_date", lookup_expr='lte')

    return_date_gte = filters.DateTimeFilter(field_name="return_date", lookup_expr='gte')
    return_date_lte = filters.DateTimeFilter(field_name="return_date", lookup_expr='lte')

    class Meta:
        model = Rental
        fields = ['book_name', 'book_unit__serial', 'rental_date', 'rental_date_gte', 'rental_date_lte',
                  'return_date', 'return_date_gte', 'return_date_lte']


def rentals_view_filters(params):
    queryset = Rental.objects.all()

    book_name = params.get('book', None)
    serial = params.get('serial', None)

    rental_date = params.get('rental_date', None)
    rental_date_gte = params.get('rental_date_gte', None)
    rental_date_lte = params.get('rental_date_lte', None)

    return_date = params.get('return_date', None)
    return_date_gte = params.get('return_date_gte', None)
    return_date_lte = params.get('return_date_lte', None)

    if book_name:
        queryset = Rental.objects.filter(book_unit__book__name__icontains=book_name)
    if serial:
        queryset = Rental.objects.filter(book_unit__serial=serial)

    # Rental date filters
    try:
        if rental_date:
            date_time = datetime.datetime.strptime(rental_date, '%Y-%m-%d')
            # Create end_date by adding a date to date_time to then filter with range
            end_date = date_time + datetime.timedelta(days=1)
            queryset = Rental.objects.filter(rental_date__range=(make_aware(date_time), make_aware(end_date)),
                                             rental_date__isnull=False)
        if rental_date_gte:
            date_time = datetime.datetime.strptime(rental_date_gte, '%Y-%m-%d')
            queryset = Rental.objects.filter(rental_date__gte=make_aware(date_time),
                                             rental_date__isnull=False)
        if rental_date_lte:
            date_time = datetime.datetime.strptime(rental_date_lte, '%Y-%m-%d')
            date_time = date_time + datetime.timedelta(days=1)
            queryset = Rental.objects.filter(rental_date__lte=make_aware(date_time),
                                             rental_date__isnull=False)
    except ValueError:
        pass

    # Return date filters
    try:
        if return_date:
            date_time = datetime.datetime.strptime(return_date, '%Y-%m-%d')
            # Create end_date by adding a date to date_time to then filter with range
            end_date = date_time + datetime.timedelta(days=1)
            queryset = Rental.objects.filter(return_date__range=(make_aware(date_time), make_aware(end_date)),
                                             return_date__isnull=False)
        if return_date_gte:
            date_time = datetime.datetime.strptime(return_date_gte, '%Y-%m-%d')
            queryset = Rental.objects.filter(return_date__gte=make_aware(date_time),
                                             return_date__isnull=False)
        if return_date_lte:
            date_time = datetime.datetime.strptime(return_date_lte, '%Y-%m-%d')
            date_time = date_time + datetime.timedelta(days=1)
            queryset = Rental.objects.filter(return_date__lte=make_aware(date_time),
                                             return_date__isnull=False)

    except ValueError:
        pass

    return queryset


def rentals_view_ordering(params, queryset):
    ordering = params.get('ordering', None)

    if ordering:
        if ordering == 'rental_date':
            queryset = queryset.order_by('rental_date')
        elif ordering == '-rental_date':
            queryset = queryset.order_by('-rental_date')
        elif ordering == 'return_date':
            queryset = queryset.order_by('return_date')
        elif ordering == '-return_date':
            queryset = queryset.order_by('-return_date')

    return queryset
