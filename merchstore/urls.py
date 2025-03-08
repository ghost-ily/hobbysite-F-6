from django.urls import path
from .views import index, ProductListView, ProductDetailView

urlpatterns = [
    path('merchstore/', index, name='index'),
    path('merchstore/items/', ProductListView.as_view(), name='list'),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name='detail'),
]

app_name = 'merchstore'