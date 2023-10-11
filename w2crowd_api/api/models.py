from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    imei = models.CharField(max_length=255)


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    sub_stock = models.CharField(max_length=255, primary_key=True)
    products = models.ManyToManyField(Product, through="WarehouseProduct")


class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class OrderSell(models.Model):
    products = models.ManyToManyField(Product, through="OrderSellProduct")
    status = models.CharField(max_length=100,default="pending")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderSellProduct(models.Model):
    order_sell = models.ForeignKey(OrderSell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
