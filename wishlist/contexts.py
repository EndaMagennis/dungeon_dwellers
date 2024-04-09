from django.conf import settings
from django.shortcuts import get_object_or_404
from profiles.models import Profile
from products.models import Product

def wishlist(request):
    """Context processor for wishlist"""
    wishlist_items = []
    # Get the wishlist from the session
    wishlist - request.session.get('wishlist', {})

    for item_id, item_data in wishlist.items():
        # If item_data is an integer, it means the item is not a product
        product = get_object_or_404(Product, pk=item_id)
        # Add the product to the wishlist_items list
        if isinstance(item_data, int):
            wishlist_items.append({
                'product_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        # If item is already in the wishlist, remove it
        else:
            wishlist_items.append({
                'product_id': item_id,
                'quantity': item_data['quantity'],
                'product': product,
            })
        

    context = {
        'wishlist_items': wishlist_items
    }

    return context


