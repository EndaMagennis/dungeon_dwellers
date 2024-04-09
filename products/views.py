from django.views import View
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.forms.formsets import formset_factory
from .forms import (
    ProductForm,
    ProductImageForm,
)
from .models import(
    Product, Category, Tag, ProductImage
)


class ProductView(View):
    """View for all products"""
    def get(self, request, *args, **kwargs):
        p = Paginator(Product.objects.all(), 32)
        page = request.GET.get('page')
        products = p.get_page(page)
        query = None
        categories = Category.objects.all()
        tags = Tag.objects.all()

        context = {
            'products': products,
            'categories': categories,
            'tags': tags,
        }
        # search using product name, description, tags, and categories
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return render(request, 'products/products.html', context)
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(tags__name__icontains=query) | Q(category__name__icontains=query)
            products = Product.objects.filter(queries)
            context = {
                'products': products,
                'categories': categories,
                'tags': tags,
            }
        return render(request, 'products/products.html', context)


class ProductDetailView(View):
    """View for individual product details"""
    def get(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(id=product_id)
        images = ProductImage.objects.filter(
            product=product,
            is_active=True    
        )

        context = {
            'product': product,
            'images': images,
        }

        return render(request, 'products/product_detail.html', context)
    

class AddProductView(View):
    """View for adding a product, category, tag, and image"""
    def get(self, request, *args, **kwargs):
        product_form = ProductForm()
        image_form = ProductImageForm()
        context = {
            'product_form': product_form,
            'image_form': image_form,
        }
        return render(request, 'products/add_product.html', context)
    
    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            image = image_form.save(commit=False)
            image.product = product
            image.save()
            return render(request, 'products/add_product.html')
        context = {
            'product_form': product_form,
            'image_form': image_form,
        }
        return render(request, 'products/add_product.html', context)

    