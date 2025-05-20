from django.contrib import admin
from .models import ProductType, Product, Transaction

# Register your models here.
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Transaction)
