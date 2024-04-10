from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug', 'created_at', 'updated_at', 'is_active', 'sku', 'rating')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Product Price',
            'category': 'Product Category',
            'tags': 'Product Tags',
            'has_dimensions': 'Has Dimensions',
            'has_quantity': 'Has Quantity',
            'is_promoted': 'Is Promoted',
            'dimensions': 'Product Dimensions',
            'quantity': 'Product Quantity',
        }

        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image', 'default_image')
        exclude = ('product', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'image': 'Product Image',
            'default_image': 'Default Image',
        }

        self.fields['image'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
    
    
