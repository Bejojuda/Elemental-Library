import datetime

from django.db import models

from books.models import BookUnit
from person.models import Person
from general.constants import Gender, Type


class Rental(models.Model):
    rental_date = models.DateField(default=datetime.date.today)
    return_date = models.DateField(blank=True, null=True)

    book_unit = models.ForeignKey(BookUnit, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    person_type = models.CharField(max_length=Type.TYPE_CHAR_LENGTH, choices=Type.TYPE_CHOICES, default=Type.STUDENT)
