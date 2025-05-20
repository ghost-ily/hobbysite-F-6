from django.urls import path
from .views import (
    index, ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView, CartListView, TransactionListView
)

urlpatterns = [
    path('merchstore/', index, name='index'),
    path('merchstore/items/', ProductListView.as_view(), name='list'),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('merchstore/item/create', ProductCreateView.as_view(), name='create'),
    path('merchstore/item/<int:pk>/edit', ProductUpdateView.as_view(), name='update'),
    path('merchstore/cart', CartListView.as_view(), name='cart'),
    path('merchstore/transactions', TransactionListView.as_view(), name='transactions')
]

app_name = 'merchstore'