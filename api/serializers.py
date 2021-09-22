from rest_framework import serializers
from .models import Category, Supplier, Product, Stock, PurchaseOrder, SaleOrder, Customer, Order, OrderDetails
from django.contrib.auth.models import User


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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'
