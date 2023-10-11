from django.urls import path, include
from rest_framework import routers
from api.views import (
    ProductViewSet,
    UploadFileView,
    WarehouseViewSet,
    WarehouseProductViewSet,
    OrderSellViewSet,
    OrderSellProductViewSet,
)

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"warehouses", WarehouseViewSet)
router.register(r"warehouses_products", WarehouseProductViewSet)
router.register(r"orders_sell", OrderSellViewSet)
router.register(r"orders_sell_products", OrderSellProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("upload_file/", UploadFileView.as_view(), name="upload_file"),
]
