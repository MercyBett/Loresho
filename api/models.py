from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name
class Supplier(models.Model):
  phone_number = models.PositiveIntegerField(unique=True)
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name
class Product(models.Model):
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  units = models.PositiveIntegerField(default=0)
  unit_price = models.PositiveIntegerField()
  quantity = models.PositiveIntegerField(default=0)
  supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Stock(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=0)

class PurchaseOrder(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  purchase_date = models.DateTimeField(auto_now_add=True)

class SaleOrder(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  staff = models.ForeignKey(User, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  # unit_price = models.DecimalField(max_digits=8,decimal_places=2)
  discount = models.DecimalField(decimal_places=2)
  date = models.DateField(auto_now_add=True)




