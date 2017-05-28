"""
Test case for category
"""
from django.test import TestCase

Base_Url = "http://127.0.0.1:8000"  # pylint: disable=invalid-name


class CategoryViewTestCase(TestCase):
    """
    Test case for category.
    """

    def test_invalid_category(self):
        """
        Test Case for Blank/Invalid Category Insertion
        """
        data = {
            "name": ""
        }
        response = self.client.post("/category/", data)
        self.assertEqual(response.status_code, 400)

    def test_valid_category(self):
        """
        Test Case for valid Category Insertion
        """
        data = {
            "name": "a"
        }
        response = self.client.post("/category/", data)
        self.assertEqual(response.status_code, 201)
