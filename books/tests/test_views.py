from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from books.models import Book, BookUnit


class BookCreationTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="Test user", password="123")

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_book_creation(self):
        data = {
            "name": "Test Book",
            "description": "A Test Book description",
            "author": []
        }

        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_creation_failed(self):
        data = {
            "author": []
        }

        response = self.client.post("/api/books/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BookUnitCreationTestCase(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(name="Book for BookUnit", description="A Book for a BookUnit")

    def test_book_unit_creation(self):
        book_id = str(self.book.id)
        response = self.client.post("/api/books/"+str(book_id)+"/")
        book_unit_id = BookUnit.objects.get(book_id=book_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response2 = self.client.get("/api/books/"+str(book_id)+"/"+str(book_unit_id)+"/")
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_book_update(self):
        book_id = str(self.book.id)
        data = {"name": "Updated Book name"}
        response = self.client.put("/api/books/"+str(book_id)+"/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Book name")

