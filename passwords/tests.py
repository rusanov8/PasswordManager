from rest_framework import status
from rest_framework.test import APITestCase

from .models import Password
from users.models import User


class TestPasswords(APITestCase):
    """
        Test case for testing Password-related functionality.
    """

    def setUp(self):

        self.user = User.objects.create_user(
            email='test@test.ru',
            password='testpassword',
        )

        self.client.force_authenticate(user=self.user)

        self.password_data = {
            'user': self.user.id,
            'password': 'testpassword',
        }

        self.service_name = 'test_service'


    def test_create_password(self):

        response = self.client.post(f'/password/{self.service_name}', self.password_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Password.objects.filter(user=self.user, service_name=self.service_name).exists())
        self.assertEqual(response.data['service_name'], self.service_name)


    def test_get_password_by_service_name(self):

        self.password_data['service_name'] = self.service_name
        self.password_data['user'] = self.user

        Password.objects.create(**self.password_data)

        response = self.client.get(f'/password/{self.service_name}', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['service_name'], self.service_name)

        expected_format = {
            'password': self.password_data['password'],
            'service_name': self.service_name,
        }

        print(type(response.data), type(expected_format))
        self.assertEqual(response.data, expected_format)


    def test_get_password_by_part_of_service_name(self):

        # test_search = 'te'
        #
        # Password.objects.create(user=self.user, service_name='test_service_1', password='password1')
        # Password.objects.create(user=self.user, service_name='test_service_2', password='password2')
        #
        # response = self.client.get(f'/password/?service_name={test_search}', format='json')
        #
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        #
        # expected_format = [
        #     {'password': 'password1', 'service_name': 'test_service_1'},
        #     {'password': 'password2', 'service_name': 'test_service_2'}
        # ]
        #
        # self.assertEqual(response.data, expected_format)
        pass

















