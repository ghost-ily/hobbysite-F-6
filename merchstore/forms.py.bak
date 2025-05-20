from django import forms
from .models import ProductType, Product, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'