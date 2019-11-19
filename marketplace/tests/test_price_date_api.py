'''
Product api tests code here
'''

import json
from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class PriceDateApiTest(TestCase):
    '''
    Product api test
    '''
    def setUp(self):
        '''
        Set up
        '''
        pass

    data = {
        "price": 12.12,
        "date_to": datetime.now().strftime('%Y-%m-%d'),
        "date_from": datetime.now().strftime('%Y-%m-%d'),
    }

    def test_price_create(self):
        '''
        Price create test
        '''
        response = self.client.post(
            reverse('product-price-set'),
            data=json.dumps(self.data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_price_get(self):
        '''
        Price get test
        '''
        response = self.client.get(
            reverse('product-price-set'),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
