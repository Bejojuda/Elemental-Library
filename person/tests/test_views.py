from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from person.models import Person


class RegistrationTestCase(APITestCase):

    def test_person_creation(self):
        data = {"username": "test_user", "password": "123", "birth_date": "2020-09-1", "gender": "O", "type": "VI"}

        response = self.client.post("/api/people/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        person = Person.objects.get(pk=response.data['id'])
        response = self.client.get('/api/people/'+str(person.id)+'/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], person.user.username)

    def test_person_creation_failed(self):
        data = {
            "username": "",
            "password": "",
            "birth_date": "",
            "gender": "",
            "type": ""
        }

        response = self.client.post("/api/people/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



