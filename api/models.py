from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    phone_number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    purchase_price = models.PositiveIntegerField(default=20)
    selling_price = models.PositiveIntegerField(default=20)
    quantity = models.PositiveIntegerField(default=1)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class PurchaseOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)


class SaleOrder(models.Model):
    product = models.ManyToManyField('Product')
    staff = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # unit_price = models.DecimalField(max_digits=8,decimal_places=2)
    discount = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        self.name


class Order(models.Model):
    order_number = models.PositiveIntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    sale_amount = models.PositiveIntegerField(default=1)
    vat = models.IntegerField(default=1)
    net_vat = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    amount_due = models.DecimalField(max_digits=8, decimal_places=2)
    change = models.DecimalField(max_digits=8, decimal_places=2)
    cashier = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)


class OrderDetails(models.Model):
    order = models.ForeignKey('Order', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=1)
