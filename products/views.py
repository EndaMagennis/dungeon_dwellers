from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
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
        p = Paginator(Product.objects.all(), 16)
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
        if request.GET:
            query = request.GET.get('search-input')
            if query:
                products = Product.objects.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query) |
                    Q(tags__name__icontains=query) |
                    Q(category__name__icontains=query)
                ).distinct()
                context = {
                    'products': products,
                    'categories': categories,
                    'tags': tags,
                    'query': query,
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
            image = request.FILES.get('image')
            image = ProductImage(image=image)
            image.product = product
            image.save()
            return redirect('products')
        context = {
            'product_form': product_form,
            'image_form': image_form,
        }
        return render(request, 'products/products.html', context)


class EditProductView(View):
    """View for editing a product"""
    def get(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(id=product_id)
        product_form = ProductForm(instance=product)
        image_form = ProductImageForm()
        context = {
            'product': product,
            'product_form': product_form,
            'image_form': image_form,
        }
        return render(request, 'products/edit_product.html', context)
    
    def post(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(id=product_id)
        product_form = ProductForm(request.POST, instance=product)
        image_form = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            image = request.FILES.get('image')
            image = ProductImage(image=image)
            image.product = product
            image.save()
            return redirect('products')
        context = {
            'product': product,
            'product_form': product_form,
            'image_form': image_form,
        }
        return render(request, 'products/products.html', context)
    

class DeleteProductView(View):
    """View for deleting a product"""
    def get(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(id=product_id)
        product.delete()
        return render(request, 'products/products.html')
    
    