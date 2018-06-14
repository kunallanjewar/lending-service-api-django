from django.test import TestCase
from .models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """Class defines test suite for out model"""

    def setUp(self):
        self.first_name = "kunal"
        self.user = User(first_name=self.first_name)

    def test_model_can_create_a_table_in_db(self):
        old_count = user.objects.count()
        self.user.save()
        new_count = user.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {'first_name': 'kunal'}
        self.response = self.client.post(
            reverse('create'),
            self.user_data,
            format = "json"
        )

    def test_api_can_create_a_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
