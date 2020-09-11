import datetime

from django.db.models.functions import Lower

from author.models import Author


def authors_view_filters(params):
    queryset = Author.objects.all()

    name = params.get('name', None)
    gender = params.get('gender', None)
    birth_date = params.get('birth_date', None)
    birth_date_gte = params.get('birth_date_gte', None)
    birth_date_lte = params.get('birth_date_lte', None)

    if name:
        queryset = Author.objects.filter(name__contains=name)

    if gender:
        queryset = Author.objects.filter(gender__iexact=gender)

    try:
        if birth_date:
            date_time = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
            queryset = Author.objects.filter(birth_date=date_time)

        if birth_date_gte:
            date_time = datetime.datetime.strptime(birth_date_gte, '%Y-%m-%d')
            queryset = Author.objects.filter(birth_date__gte=date_time)

        if birth_date_lte:
            date_time = datetime.datetime.strptime(birth_date_lte, '%Y-%m-%d')
            queryset = Author.objects.filter(birth_date__lte=date_time)
    except ValueError:
        pass

    return queryset


def authors_view_ordering(params, queryset):
    ordering = params.get('ordering', None)

    if ordering:
        if ordering == 'name':
            queryset = queryset.order_by(Lower('name'))
        elif ordering == '-name':
            queryset = queryset.order_by(Lower('name').desc())
        elif ordering == 'birth_date':
            queryset = queryset.order_by('birth_date')
        elif ordering == '-birth_date':
            queryset = queryset.order_by('-birth_date')

    return queryset
