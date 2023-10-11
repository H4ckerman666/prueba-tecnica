from traceback import print_exc
from django.db import transaction
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FileUploadParser
from .serializers import (
    OrderSellProductSerializer,
    ProductSerializer,
    WarehouseSerializer,
    OrderSellSerializer,
    WarehouseProductSerializer,
)
from api.models import OrderSellProduct, Product, Warehouse, OrderSell, WarehouseProduct
from rest_framework import status
import pandas as pd


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseProductViewSet(viewsets.ModelViewSet):
    queryset = WarehouseProduct.objects.all()
    serializer_class = WarehouseProductSerializer


class OrderSellViewSet(viewsets.ModelViewSet):
    queryset = OrderSell.objects.all()
    serializer_class = OrderSellSerializer


class OrderSellProductViewSet(viewsets.ModelViewSet):
    queryset = OrderSellProduct.objects.all()
    serializer_class = OrderSellProductSerializer


class UploadFileView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser)

    def post(self, request):
        try:
            uploaded_file = request.data["file"]
            df = pd.read_excel(uploaded_file)
            df_products = df.iloc[:, 2:-1]
            skus = df_products.columns
            rows = df.values.tolist()[:-1]
            products = df_products.values.tolist()

            with transaction.atomic():
                order_sells = []
                order_sell_products = []

                for idr, row in enumerate(rows):
                    warehouse, _ = Warehouse.objects.get_or_create(
                        sub_stock=row[0],
                        defaults={
                            "name": row[1],
                        },
                    )

                    order_sell = OrderSell(warehouse=warehouse, status="listo")
                    order_sells.append(order_sell)
                    for idx, quantity_product in enumerate(products[idr]):
                        if (
                            not isinstance(quantity_product, float)
                            or not quantity_product > 1
                        ):
                            continue
                        sku = skus[idx]

                        product, _ = Product.objects.get_or_create(
                            sku=sku,
                            defaults={"name": "", "imei": ""},
                        )

                        order_sell_product = OrderSellProduct(
                            order_sell=order_sell,
                            product=product,
                            quantity=quantity_product,
                        )
                        order_sell_products.append(order_sell_product)

                OrderSell.objects.bulk_create(order_sells)
                OrderSellProduct.objects.bulk_create(order_sell_products)

            return Response(
                {"status": "File uploaded successfully"}, status=status.HTTP_200_OK
            )
        except pd.errors.ParserError as e:
            return Response(
                {"error": "Invalid file format: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            print_exc()
            return Response(
                {"error": "An error occurred: " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
