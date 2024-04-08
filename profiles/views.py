from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Profile, Address
from .forms import ProfileForm, AddressForm

class ProfileView(View):
    """View for user profile"""
    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=request.user)
            address = Address.objects.filter(profile=profile)

            context = {
                'profile': profile,
                'address': address,
            }
            return render(request, 'profiles/profile.html', context)
        else:
            return render(request, 'account/login.html')


class ProfileUpdateView(View):
    """View for updating user profile"""
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'profiles/profile_update.html', context)
    
    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('profile', args=[request.user.username]))
        context = {
            'form': form,
        }
        return render(request, 'profiles/profile_update.html', context)
    