from django.urls import path
from .views import (
    ProductView, 
    ProductDetailView, 
    AddProductView, 
    EditProductView, 
    DeleteProductView
)

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', AddProductView.as_view(), name='add_product'),
    path('edit/<int:product_id>/', EditProductView.as_view(), name='edit_product'),
    path('delete/<int:product_id>/', DeleteProductView.as_view(), name='delete_product'),
]