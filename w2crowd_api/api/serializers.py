from rest_framework import serializers
from .models import OrderSellProduct, Product, Warehouse, OrderSell, WarehouseProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseProduct
        fields = "__all__"


class OrderSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSell
        fields = "__all__"


class OrderSellProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSellProduct
        fields = "__all__"
