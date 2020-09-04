from django.db import models

from books.models import BookUnit
from person.models import Person
from general.constants import Gender

class Rental(models.Model):
    rental_date = models.DateField(auto_created=True)
    return_date = models.DateField()

    book_unit = models.ForeignKey(BookUnit, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    person_gender = models.CharField(max_length=2, choices=Gender.GENDER_CHOICES, default=Gender.MALE)
