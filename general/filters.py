import datetime

from django.contrib.auth.models import User

from author.models import Author


def person_view_filters(params, query_model):
    queryset = query_model.objects.all()

    name = params.get('name', None)
    gender = params.get('gender', None)
    birth_date = params.get('birth_date', None)
    birth_date_gte = params.get('birth_date_gte', None)
    birth_date_lte = params.get('birth_date_lte', None)

    if query_model == User:
        if name:
            queryset = query_model.objects.filter(username__contains=name)

        if gender:
            queryset = query_model.objects.filter(person__gender__iexact=gender)

        try:
            if birth_date:
                date_time = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
                queryset = query_model.objects.filter(person__birth_date=date_time)

            if birth_date_gte:
                date_time = datetime.datetime.strptime(birth_date_gte, '%Y-%m-%d')
                queryset = query_model.objects.filter(person__birth_date__gte=date_time)

            if birth_date_lte:
                date_time = datetime.datetime.strptime(birth_date_lte, '%Y-%m-%d')
                queryset = query_model.objects.filter(person__birth_date__lte=date_time)
        except ValueError:
            pass
    else:
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
