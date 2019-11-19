'''
This file should contain admin register
'''

from django.contrib import admin
from .models import (
    Product,
    PriceDateRange,
)

admin.site.register(Product)
admin.site.register(PriceDateRange)

# Register your models here.
