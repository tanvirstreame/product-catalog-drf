from rest_framework import serializers
from .models import (
    Product,
    PriceDateRange
)


class PriceDateRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDateRange
        fields = ['id', 'price', 'date_to', 'date_from']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'code', 'slug']


class ProductAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'slug', 'code', 'name', 'price', 'extra_attribute']
        read_only_fields = ('slug',)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
