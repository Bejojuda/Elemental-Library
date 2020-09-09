from django.db import models
from rest_framework.exceptions import ValidationError

from author.models import Author


class Book(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=150)

    author = models.ManyToManyField(Author, blank=True, related_name='authors')

    def __str__(self):
        return self.name


class BookUnit(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_units')
    serial = models.CharField(max_length=16, unique=True)

    borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name + " (Serial: " + self.serial + ")"

    # Makes sure that the serial from the BookUnit does not exists
    # If it does, a ValidationError will be raised
    def save(self, *args, **kwargs):
        # Checks if the save comes from the Rental serializer or not
        # This way the ValidationError does not raise when creating a Rental
        if 'rental' not in kwargs:
            self.clean()
        # If there is an argument rental, it means it comes from rental creation,
        # so we should pop the rental from kwargs
        else:
            kwargs.pop('rental')
        super(BookUnit, self).save(*args, **kwargs)

    def clean(self):
        serial = self.serial
        exists = BookUnit.objects.filter(serial=serial).exists()

        if exists:
            raise ValidationError("The serial number already exits")
