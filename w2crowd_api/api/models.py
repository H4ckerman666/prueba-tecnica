from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    sku = models.CharField(max_length=255)
    imei = models.CharField(max_length=255)
