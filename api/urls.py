from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'stocks', views.StockViewSet)
router.register(r'purchase_orders', views.PurchaseOrderViewSet)
router.register(r'sale_orders', views.SaleOrderViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order_details', views.OrderDetailsViewSet)
router.register(r'customers', views.CustomerViewSet)
urlpatterns = [
    path('', include(router.urls)),


]
