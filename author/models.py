from django.db import models

from general.constants import Gender


class Author(models.Model):
    name = models.CharField(max_length=45)
    birth_date = models.DateField()
    gender = models.CharField(max_length=Gender.GENDER_CHAR_LENGTH, choices=Gender.GENDER_CHOICES, default=Gender.MALE)

    def __str__(self):
        return self.name
