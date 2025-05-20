from django import forms
from .models import Product, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['seller']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['buyer', 'product']
