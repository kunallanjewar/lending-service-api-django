from django.test import TestCase
from .models import *
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from faker import Faker


class ModelTestCase(TestCase):
    """Class defines test suite for our model"""

    def setUp(self):
        self.first_name = "kunal"
        self.user = User(first_name=self.first_name)

    def test_model_can_create_user_table_in_db(self):
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_account_details_table(self):
        pass

    def test_model_can_create_transactions_table_in_db(self):
        pass

class ServicesTestCase(TestCase):
    """ Test buiseness logic """
    pass

class ViewTestCase(TestCase):

    def setUp(self):
        fake = Faker()
        self.client = APIClient()
        self.user_data = {'first_name': fake.name()}
        self.response = self.client.post(
            reverse('create'),
            self.user_data,
            format = "json"
        )

    def test_api_can_create_a_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
