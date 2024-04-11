from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address_1', 'street_address_2',
            'town_or_city', 'postcode', 'country',
            'county',
        )
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Phone Number'}),
            'street_address_1': forms.TextInput(attrs={'placeholder': 'Street Address 1'}),
            'street_address_2': forms.TextInput(attrs={'placeholder': 'Street Address 2'}),
            'town_or_city': forms.TextInput(attrs={'placeholder': 'Town or City'}),
            'postcode': forms.TextInput(attrs={'placeholder': 'Postcode'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'county': forms.TextInput(attrs={'placeholder': 'County'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False