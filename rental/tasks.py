from __future__ import absolute_import, unicode_literals

import datetime

from celery import shared_task
from django.utils.timezone import make_aware

from rental.models import Rental


# The decorator allows this function to be registered as a celery task (and show up on Django Admin)
@shared_task
def check_rentals_return():
    """
    Check Rentals rental_date, if a certain time has passed, the return_date is set to the current
    date and the BookUnit borrowed attribute is set to false
    """
    today = datetime.datetime.today()
    past = today - datetime.timedelta(hours=7)
    rentals = Rental.objects.filter(return_date__isnull=True, rental_date__gte=make_aware(past))

    expected_time = today - datetime.timedelta(minutes=1)
    expected_time += datetime.timedelta(hours=5)
    for rental in rentals:
        if rental.rental_date < make_aware(expected_time):
            now = datetime.datetime.now() + datetime.timedelta(hours=5)
            rental.return_date = make_aware(now)
            rental.save()

    return None
