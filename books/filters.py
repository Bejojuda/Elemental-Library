from distutils.util import strtobool

from django.db.models.functions import Lower

from books.models import Book, BookUnit


def books_view_filters(params):
    queryset = Book.objects.all()

    name = params.get('name', None)
    author = params.get('author', None)

    if name:
        queryset = Book.objects.filter(name__icontains=name)
    elif author:
        queryset = Book.objects.filter(author__name__icontains=author)

    return queryset


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


def book_units_view_filters(params):
    queryset = BookUnit.objects.all()
    serial = params.get('serial', None)
    borrowed = params.get('borrowed', None)

    if serial:
        queryset = BookUnit.objects.filter(serial__iexact=serial)
    if borrowed:
        try:
            borrowed = strtobool(borrowed)

            queryset = BookUnit.objects.filter(borrowed=borrowed)
        except ValueError:
            print("Error")

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
