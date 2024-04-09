from django.urls import path
from .views import ProductView, ProductDetailView, AddProductView


urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', AddProductView.as_view(), name='add_product'),
]