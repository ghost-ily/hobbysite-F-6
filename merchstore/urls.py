from django.urls import path
from .views import (
    index, ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView
)

urlpatterns = [
    path('merchstore/', index, name='index'),
    path('merchstore/items/', ProductListView.as_view(), name='list'),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('merchstore/item/create', ProductCreateView.as_view(), name='create'),
    path('merchstore/item/<int:pk>/edit', ProductUpdateView.as_view(), name='update'),
]

app_name = 'merchstore'