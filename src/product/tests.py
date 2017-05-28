"""
Test for product
"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client

Base_Url = "http://127.0.0.1:8000"  # pylint: disable=invalid-name


class ProductViewTestCase(TestCase):
    """
    Test case for product view.
    """

    def test_valid_category(self):
        """
        Test Case for valid Category Insertion
        """
        self.client = Client()  # pylint: disable=attribute-defined-outside-init
        self.user = User.objects.create(  # pylint: disable=no-member,attribute-defined-outside-init
            username="xyz123456",
            email="aaditi.d@amazatic.com"
        )
        self.user.set_password('xyz123456')
        self.user.save()
        login = self.client.login(username=self.user.username,
                                  password='xyz123456')
        self.assertTrue(login, True)
        data = {
            "name": "amazatic",
            "parent": ""
        }
        response = self.client.post("/category/", data)
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/category/1/")
        self.assertEqual(response.status_code, 200)

    def test_invalid_category(self):
        """
        Test Case for Blank/Invalid Category Insertion
        """
        self.client = Client()  # pylint: disable=attribute-defined-outside-init
        self.user = User.objects.create(  # pylint: disable=no-member,attribute-defined-outside-init
            username="pqrs",
            email="aaditi.d@amazatic.com"
        )
        self.user.set_password('pqrst123')
        self.user.save()
        login = self.client.login(username=self.user.username,
                                  password='pqrst123')
        self.assertTrue(login, True)
        data = {
            "id": 1,
            "sku_number": "1",
            "category": {
                "id": 1,
                "name": "1",
                "parent": "null"
            },
            "name": "test",
            "condition": "new",
            "origin": "china",
            "description": "<p>test</p>",
            "price_details": {
                "id": 1,
                "cost": "1.00",
                "wholesale": "1.00",
                "sale": "1.00"
            },
            "shipping_details": {
                "id": 1,
                "dimension_uom": "cm",
                "length": "1.00",
                "height": "1.00",
                "width": "1.00",
                "weight_uom": "kg",
                "weight": "1.00",
                "package_type": "parcel"
            }
        }
        response = self.client.post("/product/", data)
        self.assertEqual(response.status_code, 400)
