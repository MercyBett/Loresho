from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Supplier)
admin.site.register(models.Product)
admin.site.register(models.Stock)
admin.site.register(models.PurchaseOrder)
admin.site.register(models.SaleOrder)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderDetails)
