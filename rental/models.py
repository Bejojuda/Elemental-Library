from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from books.models import BookUnit
from person.models import Person
from general.constants import Type


class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)

    book_unit = models.ForeignKey(BookUnit, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    person_type = models.CharField(max_length=Type.TYPE_CHAR_LENGTH, choices=Type.TYPE_CHOICES, default=Type.STUDENT)


# Signal used to change the Book Unit borrowed attribute to True when a Rental is created
@receiver(post_save, sender=Rental)
def make_book_borrowed(sender, **kwargs):
    if kwargs.get('created', False):
        book_unit_id = kwargs['instance'].book_unit_id
        book_unit = BookUnit.objects.get(pk=book_unit_id)
        book_unit.borrowed = True
        book_unit.save()


@receiver(post_delete, sender=Rental)
def rental_deleted(sender, instance, **kwargs):
    book_unit = BookUnit.objects.get(pk=instance.book_unit.id)
    book_unit.borrowed = False
    book_unit.save(rental=True)

