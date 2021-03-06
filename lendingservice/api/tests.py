from django.test import TestCase
from django.contrib.auth.models import User
from .models import User as UserModel, AccountDetail, Transaction
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from faker import Faker


class ModelTestCase(TestCase):
    """Class defines test suite for our model"""

    def setUp(self):
        self.fake = Faker()
        user = User.objects.create(username=self.fake.user_name())

        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.email = self.fake.email()

        self.user_data = UserModel(
            owner=user,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
        )

    def test_model_can_create_user_table_in_db(self):
        old_count = UserModel.objects.count()
        self.user_data.save()
        new_count = UserModel.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_account_details_table(self):
        pass

    def test_model_can_create__table_in_db(self):
        pass

class ServicesTestCase(TestCase):
    """ Test buiseness logic here """
    pass

class ViewTestCase(TestCase):

    def setUp(self):
        self.fake = Faker()
        user = User.objects.create(username=self.fake.user_name())

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.user_data = {
                'owner':user.id,
                'first_name': self.fake.first_name(),
                'last_name': self.fake.last_name(),
                'email': self.fake.email(),
        }
        self.response = self.client.post(
                reverse('createuser'),
                self.user_data,
                format = "json"
        )

    def test_api_can_create_a_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        a_client = APIClient()
        a_response = a_client.get(
                'profile',
                kwargs={'pk':5},
                format="json",
        )
        self.assertEqual(a_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_user_details(self):
        user = UserModel.objects.get(id=5)

        response = self.client.get(
                'profile',
                kwargs={'pk':user.id},
                format="json",

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)

    def test_api_can_update_user_email(self):
        user = UserModel.objects.get()
        change_email = {'email':'hello@test.com'}
        response = self.client.put(
                reverse('profile', kwargs={'pk':user.id}),
                change_email,
                format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_user(self):
        pass
