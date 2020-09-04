from django.db import models

from author.models import Author


class Book(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=150)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookUnit(Book):
    serial = models.IntegerField(unique=True)
