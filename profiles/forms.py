from django import forms
from .models import Profile, Address


class ProfileForm(forms.ModelForm):
    """Form for user profile"""
    class Meta:
        """Meta class for ProfileForm"""
        model = Profile
        fields = ['first_name', 'last_name', 'avatar']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'avatar': 'Avatar',
        }
        exclude = ('user', 'created_at', 'updated_at')

    def __init__(self, *args, **kwargs):
        """Constructor for ProfileForm"""
        super().__init__(*args, **kwargs)

        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control-file'})

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class AddressForm(forms.ModelForm):
    """Form for user address"""
    class Meta:
        """Meta class for AddressForm"""
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'county', 'post_code', 'country']
        labels = {
            'address_line_1': 'Street Address 1',
            'address_line_2': 'Street Address 2',
            'city': 'Town or City',
            'county': 'County',
            'post_code': 'Postcode',
            'country': 'Country',
        }
        exclude = ('profile',)

    def __init__(self, *args, **kwargs):
        """Constructor for AddressForm"""
        super().__init__(*args, **kwargs)

        placeholders = {
            'address_line_1': 'Street Address 1',
            'address_line_2': 'Street Address 2',
            'county': 'County',
            'city': 'Town or City',
            'post_code': 'Postcode',
            'country': 'Country',
        }

        self.fields['address_line_1'].widget.attrs.update({'autofocus': 'autofocus'})
        # iterate over the fields in the form
        for field in self.fields:
            # if the field is required, add a * to the placeholder
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                # if the field is not required, set the placeholder to the value in the placeholders dictionary
                placeholder = placeholders[field]
            # set the placeholder attribute of the field to the value of the placeholder variable
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # set the class attribute of the field to 'border-black rounded-0 profile-form-input'
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            # set the label attribute of the field to False
            self.fields[field].label = False

