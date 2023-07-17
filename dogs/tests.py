import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dogs.models import Category, Dog


class DogTestCase(APITestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(
            name='test'
        )

        self.dog = Dog.objects.create(
            name='test',
            category=self.category
        )

    def test_get_list(self):
        """ Test for getting list of dogs """

        response = self.client.get(
            reverse('dogs:list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.dog.id,
                        "name": self.dog.name,
                        "phot": self.dog.phot,
                        "birth_day": self.dog.birth_day,
                        "category": self.dog.category_id,
                        "owner": self.dog.owner
                    }
                ]
            }
        )

    def test_dog_create(self):
        """ Test dog creating """

        data = {
            'name': 'test2',
            'category': self.category.id
        }

        response = self.client.post(
            reverse('dogs:dog_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Dog.objects.all().count(),
            2
        )

    def test_dog_create_validation_error(self):
        """ Test validation error """

        data = {
            'name': 'крипта',
            'category': self.category.id
        }

        response = self.client.post(
            reverse('dogs:dog_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'name': ['Использованы запрещенные слова!']}
        )
