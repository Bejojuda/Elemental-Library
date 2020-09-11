import datetime

from django.contrib.auth.models import User
from django.db.models.functions import Lower


def person_view_filters(params):
    queryset = User.objects.all()

    name = params.get('name', None)
    gender = params.get('gender', None)
    birth_date = params.get('birth_date', None)
    birth_date_gte = params.get('birth_date_gte', None)
    birth_date_lte = params.get('birth_date_lte', None)

    if name:
        queryset = User.objects.filter(username__contains=name)

    if gender:
        queryset = User.objects.filter(person__gender__iexact=gender)

    try:
        if birth_date:
            date_time = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
            queryset = User.objects.filter(person__birth_date=date_time)

        if birth_date_gte:
            date_time = datetime.datetime.strptime(birth_date_gte, '%Y-%m-%d')
            queryset = User.objects.filter(person__birth_date__gte=date_time)

        if birth_date_lte:
            date_time = datetime.datetime.strptime(birth_date_lte, '%Y-%m-%d')
            queryset = User.objects.filter(person__birth_date__lte=date_time)
    except ValueError:
        pass

    return queryset


def person_view_ordering(params, queryset):
    ordering = params.get('ordering', None)

    if ordering:
        if ordering == 'name':
            queryset = queryset.order_by(Lower('username'))
        elif ordering == '-name':
            queryset = queryset.order_by(Lower('username').desc())
        elif ordering == 'birth_date':
            queryset = queryset.order_by('person__birth_date')
        elif ordering == '-birth_date':
            queryset = queryset.order_by('-person__birth_date')

    return queryset
