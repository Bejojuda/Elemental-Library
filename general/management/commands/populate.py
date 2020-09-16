import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from random_username.generate import generate_username
from django.utils.crypto import get_random_string
from faker import Faker

from general.constants import Gender, Type
from person.models import Person


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def populate_people(self, amount):
        fake = Faker()
        for _ in range(amount):
            username = generate_username()[0]
            password = make_password(get_random_string(random.randint(8, 15)))
            #user = User.objects.create(username=username, password=password)
            #print(user.__dict__)
            birth_date = fake.date_of_birth(minimum_age=15, maximum_age=100)
            gender = random.choice(list(Gender.GENDER_CHOICES))
            type = random.choice(list(Type.TYPE_CHOICES))
            type=[element for tupl in Gender.GENDER_CHOICES for element in tupl]
            print(type)
            #person = Person.objects.create(user=user, birth_date=birth_date, gender=gender, type=type)
            #print(person.__dict__)

    def handle(self, *args, **options):
        self.populate_people(random.randint(1, 1))
