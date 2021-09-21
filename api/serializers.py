from rest_framework import serializers
from .models import Category, Supplier, Product, Stock, PurchaseOrder, SaleOrder


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class SaleOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaleOrder
        fields = '__all__'
