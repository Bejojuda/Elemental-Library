from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from author.models import Author


class AuthorCreationTestCase(APITestCase):

    def test_author_creation(self):
        data = {"name": "Test Author", "birth_date": "2020-09-1", "gender": "F", }

        response = self.client.post("/api/authors/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author = Author.objects.get(pk=response.data['id'])
        response = self.client.get('/api/authors/'+str(author.id)+'/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], author.name)

    def test_person_creation_failed(self):
        data = {
            "name": "",
            "password": "",
            "birth_date": "",
            "gender": ""
        }

        response = self.client.post("/api/authors/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
