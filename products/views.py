from django.shortcuts import render
from .models import Product, Category, Tag, ProductImage

# Create your views here.
def all_products(request):
    """A view to show all products, including sorting and search queries."""
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """A view to show individual product details."""
    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product=product)

    context = {
        'product': product,
        'images': images,
    }

    return render(request, 'products/product_detail.html', context)


