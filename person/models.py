from django.db import models
from django.contrib.auth.models import User

from general.constants import Gender, Type
from django.db.models.signals import post_save
from django.dispatch import receiver


class Person(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                )

    birth_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=Gender.GENDER_CHAR_LENGTH, choices=Gender.GENDER_CHOICES, default=Gender.MALE)
    type = models.CharField(max_length=Type.TYPE_CHAR_LENGTH, choices=Type.TYPE_CHOICES, default=Type.VISITOR)

    def __str__(self):
        return self.user.username
