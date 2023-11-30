from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class TestUserCreation(APITestCase):
    """
        Test case for user creation.
    """

    def setUp(self):

        self.user_data = {
            'email': 'test@test.ru',
            'password': 'testpassword'
        }

    def test_create_user(self):

        response = self.client.post('/users/create/', self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=self.user_data['email']).exists())
        self.assertEqual(response.data['email'], self.user_data['email'])



