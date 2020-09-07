from django.db import models

from author.models import Author


class Book(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=150)

    author = models.ManyToManyField(Author, blank=True, related_name='authors')

    def __str__(self):
        return self.name


class BookUnit(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_units')
    serial = models.CharField(max_length=16)

    def __str__(self):
        return self.book.name
