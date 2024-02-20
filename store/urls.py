# store/urls.py

from django.urls import path
from .views import ProductList, CustomerList, OrderList, TotalRevenue, APIRoot

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),  # Empty path for the default root view
    path('products/', ProductList.as_view(), name='product-list'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('total-revenue/', TotalRevenue.as_view(), name='total-revenue'),
]
