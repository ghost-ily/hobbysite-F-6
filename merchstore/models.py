from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=999, decimal_places=2)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        related_name = 'product_type'
    )
    
    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        return reverse('merchstore:detail', args=[self.pk])
    
    def __str__(self):
        return self.name