from django.urls import path
from .views import ProfileView


urlpatterns = [
    path('<str:user>/', ProfileView.as_view(), name='profile'),
]
