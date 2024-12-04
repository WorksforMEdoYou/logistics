# inventory/urls.py
from django.urls import path
from .views import (
    product_list,
    product_detail,
    supplier_list,
    supplier_detail,
    inventory_list,
    inventory_detail,
    inventory_report,
    inventory_movements,
    supplier_order_history,
    RegisterView,
    CustomTokenObtainPairView,
)

urlpatterns = [
    # Product URLs
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),

    # Supplier URLs
    path('suppliers/', supplier_list, name='supplier_list'),
    path('suppliers/<int:pk>/', supplier_detail, name='supplier_detail'),

    # Inventory URLs
    path('inventory/', inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', inventory_detail, name='inventory_detail'),

    # Reporting URLs
    path('inventory/report/', inventory_report, name='inventory_report'),
    path('inventory/movements/<str:start_date>/<str:end_date>/', inventory_movements, name='inventory_movements'),
    path('suppliers/<int:supplier_id>/orders/', supplier_order_history, name='supplier_order_history'),

    # User URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]