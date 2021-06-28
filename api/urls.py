from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product-list/', views.product_list, name="product_list"),
    path('product-detail/<str:pk>', views.product_detail, name="product_detail"),
    path('product-create/', views.product_create, name="product_create"),
    path('product-update/<str:pk>', views.product_update, name="product_update"),
    path('product-delete/<str:pk>', views.product_delete, name="product_delete"),

]
