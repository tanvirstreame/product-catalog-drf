'''
This file should contain views
'''

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import (
    ProductSerializer,
    ProductAllSerializer,
    PriceDateRangeSerializer
)
from .models import (
    Product,
    PriceDateRange
)
# Create your views here.

class ProductList(generics.ListCreateAPIView):
    '''
    Fetch list of all product and create product here
    '''
    serializer_class = ProductAllSerializer
    queryset = Product.objects.all()

class ProductDetail(generics.RetrieveAPIView):
    '''
    Get single product detail by id
    '''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductAttribute(generics.RetrieveAPIView):
    '''
    Retrieve single product and patch attribute
    '''
    serializer_class = ProductAllSerializer
    queryset = Product.objects.all()

    def patch(self, request, **kwargs):
        '''
        Add extra attribute to product such as color,
        size, others dynamically using patch method
        '''
        extra = {}
        for key in request.data.keys():
            extra[key] = request.data[key]
        product_instance = get_object_or_404(Product, id=kwargs['pk'])
        serializer = ProductAllSerializer(product_instance, data={"extra_attribute": extra}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProductPriceDateSet(generics.ListCreateAPIView):
    '''
    Add price for a certain date range
    '''
    serializer_class = PriceDateRangeSerializer
    queryset = PriceDateRange.objects.all()


class ProductPriceAssign(generics.RetrieveAPIView):
    '''
    Retrieve single product
    '''
    serializer_class = ProductAllSerializer
    queryset = Product.objects.all()

    def patch(self, request, **kwargs):
        '''
        Assign price id to product price property
        '''
        product_instance = get_object_or_404(Product, id=kwargs['pk'])
        serializers = ProductAllSerializer(product_instance, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
