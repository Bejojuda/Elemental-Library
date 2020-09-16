import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from random_username.generate import generate_username
from django.utils.crypto import get_random_string
from faker import Faker

from general.constants import Gender


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def populate_people(self, amount):
        fake = Faker()
        for _ in range(amount):
            username = generate_username()[0]
            password = get_random_string(random.randint(8, 15))
            # user = User.objects.create(username=username, password=password)

            birth_date = fake.date_of_birth(minimum_age=15, maximum_age=100)
            gender = random.choice(Gender.GENDER_CHOICES)
            print(gender)

    def handle(self, *args, **options):
        self.populate_people(random.randint(1, 1))
