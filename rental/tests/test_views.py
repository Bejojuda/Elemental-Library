from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from books.models import BookUnit, Book


class RentalCreationTestCase(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(name="A test Book", description="A Book")
        self.book_unit = BookUnit.objects.create(book=self.book, serial="TestSerialNumber")
        data = {"username": "test_user", "password": "123", "birth_date": "2020-09-1", "gender": "O", "type": "VI"}
        self.person = self.client.post("/api/people/", data).data
        self.client = APIClient()
        self.user = User.objects.get(username=self.person['username'])
        self.client.force_authenticate(user=self.user)

    def test_rental_creation(self):
        book_unit = {
            "book_unit": self.book.id
        }
        response = self.client.post("/api/rentals/borrow/", book_unit)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rental_creation_failed(self):
        response = self.client.post("/api/rentals/borrow/", {})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_return_book_unit(self):
        book_unit = {
            "book_unit": self.book.id
        }
        rental_response = self.client.post("/api/rentals/borrow/", book_unit)
        return_response = self.client.put("/api/rentals/return/"+str(rental_response.data['id'])+"/")

        self.assertEqual(return_response.status_code, status.HTTP_200_OK)


