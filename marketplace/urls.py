'''
This file should contain the marketplace url
'''

from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    ProductAttribute,
    ProductPriceDateSet,
    ProductPriceAssign,
)

urlpatterns = [
    path(
        'products/',
        ProductList.as_view(),
        name='product-list'
    ), # Use get method to fetch product
    path(
        'products/<int:pk>/',
        ProductDetail.as_view(),
        name='product-detail'
    ), # Use get method to get single product detail
    path(
        'products/<int:pk>/attributes/',
        ProductAttribute.as_view(),
        name='product-attributes'
    ), # Use patch method to add extra attribute of product
    path(
        'product-prices-date-set/',
        ProductPriceDateSet.as_view(),
        name='product-price-set'
    ), # Use post method to set price and date range
    path(
        'products/<int:pk>/prices/',
        ProductPriceAssign.as_view(),
        name='product-price-assign'
    ), # Use patch method to assing price to price model
]
