import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from random_username.generate import generate_username
from django.utils.crypto import get_random_string
from faker import Faker

from author.models import Author
from books.models import Book, BookUnit
from general.constants import Gender, Type
from person.models import Person
from rental.models import Rental


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        self.populate_people(random.randint(1, 10))
        self.populate_authors(random.randint(1, 10))
        self.populate_books(random.randint(1, 15))
        self.populate_book_units(random.randint(1, 50))
        self.populate_rentals(random.randint(1, 30))

    def populate_rentals(self, amount):
        fake = Faker()
        for _ in range(amount):
            book_units = BookUnit.objects.all()
            while True:
                random_book_unit = random.choice(book_units)
                if not random_book_unit.borrowed:
                    break

            people = Person.objects.all()
            person = random.choice(list(people))
            person_type = person.type

            rental_date = fake.date_between(start_date='-1y', end_date='today')
            percentage = random.randint(1, 100)
            return_date = None

            if percentage < 40:
                while True:
                    return_date = fake.date_between(start_date='-1y', end_date='today')

                    if return_date > rental_date:
                        break

                random_book_unit.borrowed = False
            else:
                random_book_unit.borrowed = True

            random_book_unit.save()
            if return_date:
                rental = Rental.objects.create(book_unit=random_book_unit, person=person, person_type=person_type,
                                               rental_date=rental_date, return_date=return_date)
                rental.rental_date = rental_date
                rental.save()
            else:
                rental = Rental.objects.create(book_unit=random_book_unit, person=person, person_type=person_type,
                                               rental_date=rental_date)

    def populate_book_units(self, amount):
        for _ in range(amount):
            books = Book.objects.all()
            random_book = random.choice(books)

            serial = get_random_string(length=16)

            book_unit = BookUnit.objects.create(book=random_book, serial=serial)

    def populate_books(self, amount):
        fake = Faker()
        for _ in range(amount):
            name = fake.name()
            description = fake.text()

            authors = Author.objects.all()

            random_authors = random.sample(list(authors), random.randint(0, 3))

            book = Book.objects.create(name=name, description=description)

            book.author.add(*random_authors)

            book.save()

    def populate_authors(self, amount):
        for _ in range(amount):
            fake = Faker()
            name = fake.name()

            birth_date = fake.date_of_birth(minimum_age=15, maximum_age=60)

            gender_choices = [element for tuple in Gender.GENDER_CHOICES for element in tuple][::2]
            gender = random.choice(gender_choices)

            author = Author.objects.create(name=name, birth_date=birth_date, gender=gender)

    def populate_people(self, amount):
        for _ in range(amount):
            username = generate_username()[0]
            password = make_password(get_random_string(random.randint(8, 15)))
            user = User.objects.create(username=username, password=password)

            fake = Faker()
            birth_date = fake.date_of_birth(minimum_age=15, maximum_age=60)

            gender_choices = [element for tuple in Gender.GENDER_CHOICES for element in tuple][::2]
            gender = random.choice(gender_choices)

            type_choices = [element for tuple in Type.TYPE_CHOICES for element in tuple][::2]
            type = random.choice(type_choices)

            person = Person.objects.create(user=user, birth_date=birth_date, gender=gender, type=type)
