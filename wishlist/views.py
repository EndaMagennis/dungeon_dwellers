from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Wishlist
from products.models import Product

class WishlistView(View):
    """View for user wishlist"""
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            wishlist = get_object_or_404(Wishlist, user=request.user)
            products = wishlist.get_products()
            total = wishlist.get_wishlist_total()
            total_price = wishlist.get_wishlist_total_price()
            context = {
                'wishlist': wishlist,
                'products': products,
                'total': total,
                'total_price': total_price,
            }
            return render(request, 'wishlist/wishlist.html', context)
        else:
            return render(request, 'account/login.html')


class AddRemoveWishlistView(View):
    """View for adding and removing products from wishlist"""
    def post(self, request, *args, **kwargs):
        ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if request.user.is_authenticated:
            product_id = request.POST.get('product_id')
            product = get_object_or_404(Product, id=product_id)
            wishlist = get_object_or_404(Wishlist, user=request.user)
            action = request.POST.get('action')
            if action == 'add':
                wishlist.add_to_wishlist(product)
                messages.success(request, f'{product.name} added to wishlist')
            elif action == 'remove':
                wishlist.remove_from_wishlist(product)
                messages.success(request, f'{product.name} removed from wishlist')
            return redirect('wishlist')
        else:
            return render(request, 'account/login.html')


class ClearWishlistView(View):
    """View for clearing wishlist"""
    def post(self, request, *args, **kwargs):
        ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if request.user.is_authenticated and ajax:
            wishlist = get_object_or_404(Wishlist, user=request.user)
            wishlist.clear_wishlist()
            messages.success(request, 'Wishlist cleared')
            return redirect('wishlist')
        else:
            return render(request, 'account/login.html')
        

