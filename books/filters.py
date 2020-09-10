from books.models import Book


def books_view_filters(params):
    queryset = Book.objects.all()

    name = params.get('name', None)
    author = params.get('author', None)

    if name:
        queryset = Book.objects.filter(name__icontains=name)
    elif author:
        queryset = Book.objects.filter(author__name__icontains=author)

    return queryset
