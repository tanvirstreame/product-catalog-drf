'''
Product api tests code here
'''
import json
from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from faker import Faker


class ProductApiTest(TestCase):
    '''
    Product api test
    '''

    fake = Faker()
    def setUp(self):
        '''
        Set up
        '''
        pass

    def price_date_set(self):
        '''
        Reusing price date endpoint call in a function
        '''
        price_data = {
            "price": 12.12,
            "date_to": datetime.now().strftime('%Y-%m-%d'),
            "date_from": datetime.now().strftime('%Y-%m-%d'),
        }
        price_response = self.client.post(
            reverse('product-price-set'),
            data=json.dumps(price_data),
            content_type='application/json'
        )

        return price_response

    def product_create(self):
        '''
        Reusing product_create endpoint call in a function
        '''
        data = {
            'code': self.fake.name(),
            'name': self.fake.name(),
            'price': self.price_date_set().data['id'],
            'extra_attribute': {},
        }

        response = self.client.post(
            reverse('product-list'),
            data=json.dumps(data),
            content_type='application/json'
        )

        return response

    def test_product_create(self):
        '''
        Product create test
        '''
        self.assertEqual(self.product_create().status_code, status.HTTP_201_CREATED)

    def test_product_get(self):
        '''
        Product fetch test
        '''
        response = self.client.get(
            reverse('product-list'),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_set_extra_attribute(self):
        '''
        Product set extra attribute test
        '''
        extra_attribute_data = {
            "color": "black"
        }
        priduct_id = str(self.product_create().data['id'])
        response = self.client.patch(
            '/api/v1/products/' + priduct_id + '/attributes/',
            data=json.dumps(extra_attribute_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check exact equal
        self.assertEqual(response.data['extra_attribute'], extra_attribute_data)

    def test_assign_price_to_product(self):
        '''
        Product assign price to product test
        '''
        price_data = {
            "price": self.price_date_set().data["id"]
        }
        product_id = str(self.product_create().data['id'])
        response = self.client.patch(
            '/api/v1/products/' + product_id + '/prices/',
            data=json.dumps(price_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Check exact equal
        self.assertEqual(response.data['price'], price_data['price'])

