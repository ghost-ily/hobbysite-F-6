from django.urls import path
from django.contrib.auth import views as auth_views

from .views import display_home, create_user

urlpatterns = [
    path('', display_home, name='home'),
    path('register', create_user, name='register'),
]