from django.test import TestCase
from django.contrib.auth.models import User
from .models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from faker import Faker


class ModelTestCase(TestCase):
    """Class defines test suite for our model"""

    def setUp(self):
        self.fake = Faker()

        username = User.objects.create(username=self.fake.user_name())
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.email = self.fake.email()

        self.user_data = User(
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
        )

    def test_model_can_create_user_table_in_db(self):
        old_count = User.objects.count()
        self.user_data.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_account_details_table(self):
        pass

    def test_model_can_create_transactions_table_in_db(self):
        pass

class ServicesTestCase(TestCase):
    """ Test buiseness logic here """
    pass

class ViewTestCase(TestCase):

    def setUp(self):
        username = User.objects.create(username="superman")

        self.fake = Faker()
        self.client = APIClient()
        self.client.force_authentication(user=username)

        self.user_data = {
                'first_name': self.fake.first_name(),
                'last_name': self.fake.last_name(),
                'email': self.fake.email()
        }
        self.response = self.client.post(
            reverse('create'),
            self.user_data,
            format = "json"
        )

    def test_api_can_create_a_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        client = APIClient()
        response = client.get(
                '/api/',
                kwargs={'pk':3},
                format="json",
        )
        self.assertEqual(repsonse.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_user(self):
        pass

    def test_api_can_update_user_email(self):
        pass

    def test_api_can_delete_user(self):
        pass
