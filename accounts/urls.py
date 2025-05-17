from django.urls import path

from .views import display_home

urlpatterns = [
    path('', display_home, name='home')
]