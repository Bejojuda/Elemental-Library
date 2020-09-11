from distutils.util import strtobool

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


def book_unit_view_filters(params):
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
