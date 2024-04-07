from django.contrib import admin
from .models import (
    Category,
    Tag,
    Product,
    ProductImage
)

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name', 'created_at', 'updated_at')
    search_fields = ('name', 'friendly_name')
    ordering = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name', 'created_at')
    search_fields = ('name', 'friendly_name')
    ordering = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'category', 'price')
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',), 'sku': ('name',)}

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'created_at', 'updated_at')
    search_fields = ('product', 'image')
    ordering = ('product',)