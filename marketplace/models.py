'''
This file should contain models
'''

from django.db import models
import jsonfield
from django.template.defaultfilters import slugify

# Create your models here.

class PriceDateRange(models.Model):
    '''
    PriceDateRange model is here. Using this
    models we can set price for a specific
    date range
    '''
    price = models.DecimalField(max_digits=19, decimal_places=2)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return "Id: {}, Price: {}".format(self.id, self.price)


class Product(models.Model):
    '''
    Product model is here
    '''
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True)
    price = models.ForeignKey(PriceDateRange, on_delete=models.DO_NOTHING, default=1, blank=True)
    extra_attribute = jsonfield.JSONField(blank=True)

    def save(self, *args, **kwargs):
        '''
        Slugifying product code value as slug as
        it will be unique
        '''
        self.slug = slugify(self.code)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return "Id: {}, Name: {}".format(self.id, self.name)
