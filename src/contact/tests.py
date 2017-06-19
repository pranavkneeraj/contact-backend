"""
Test for athuntication.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from authentication.serializers import (
    LogInSerializer)

from knox.models import AuthToken


# .................................................................................................... Test cases for Views


class LoginTestCase(TestCase):
    """
    Test case for login.
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(  # pylint: disable=no-member
            username="adt",
            email="aaditi.d@amazatic.com"
        )
        self.user.set_password('qwerty123')
        self.user.save()

    def tearDown(self):
        self.user.delete()
        self.client.logout()

    def test_user_logged_in(self):
        """
        Should return true for user is logged in
        """
        login = self.client.login(username=self.user.username,
                                  password='qwerty123')
        self.assertTrue(login, True)
        print("User logged in", login)

    def test_invalid_logged_in(self):
        """
        Should return false when user is logged in
        """
        login = self.client.login(username=self.user.username,
                                  password='qwerty')
        self.assertFalse(login, False)
        print("Invalid user", login)

# .................................................................................................... Test cases for Serializer


class TestLoginSerializer(TestCase):
    """
    Test for login with valid and invalid case.
    """
    def setUp(self):
        self.user = User.objects.create(  # pylint: disable=no-member
            username="adt"
        )
        self.user.set_password("qwerty123")
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_valid_login(self):
        """
        Test case for valid login details.
        """

        data = {
            'username': "adt",
            'password': "qwerty123"
        }

        response = self.client.post("http://127.0.0.1:8000/auth/login",
                                    data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        """
        Test case for invalid login details.
        """
        data = {
            'username': "adt123",
            'password': "qwerty123"
        }
        expected_error = {
            'non_field_errors': [
                'Invalid Username.'
            ]
        }
        serializer = LogInSerializer(data=data, many=False)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(serializer.errors, expected_error)
        print("Invalid user", serializer.errors)

    def test_logout_deletes_keys(self):
        """
        Logout Test Case
        """
        self.assertEqual(AuthToken.objects.count(), 0)  # pylint: disable=no-member
        username, password = 'adt123', 'qwerty123'
        user = User.objects.create_user(username, 'root@localhost.com', password)
        AuthToken.objects.create(user=user)
        self.assertEqual(AuthToken.objects.count(), 1)  # pylint: disable=no-member

    def test_forgot_password(self):
        """
        Test case for forgot password.
        """
        data = {
            'email': 'aaditi.d@amazatic.com',
        }
        response = self.client.post("http://127.0.0.1:8000/auth/forgot-password",
                                    data)
        self.assertEqual(response.status_code, 400)
