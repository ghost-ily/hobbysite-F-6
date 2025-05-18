from django import forms
from .models import ProductType, Product, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',
                  'product_type', 'owner', 'stock', 'status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs['readonly'] = 'readonly'
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'