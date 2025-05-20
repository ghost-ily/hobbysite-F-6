from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Product(models.Model):
    class State(models.TextChoices):
        AVAILABLE = 'AVAILABLE', "Available"
        SALE = 'ON SALE', "On Sale"
        UNAVAILABLE = 'UNAVAILABLE', "Out of Stock"

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=999, decimal_places=2)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_type'
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='owner',
    )
    stock = models.IntegerField()

    status = models.CharField(max_length=20, choices=State.choices, default=State.AVAILABLE)
    
    class Meta:
        ordering = ['name']
    
    def set_product_status(self):
        if self.object.filter(pk=self.pk).get(self.stock) == 0:
            self.status = self.State.UNAVAILABLE
            self.save()
        else:
            self.status = self.State.AVAILABLE
            self.save()

    def get_absolute_url(self):
        return reverse('merchstore:detail', args=[self.pk])
    
    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    class DeliveryState(models.TextChoices):
        CART = 'ON CART', "On Cart"
        PAY = 'TO PAY', "To Pay"
        SHIP = 'TO SHIP', "To Ship"
        RECEIVE = 'TO RECEIVE', "To Recieve"
        DELIVERED = 'DELIVERED', "Delivered"

    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='buyer'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_bought'
    )
    amount = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=20, choices=DeliveryState.choices, default=DeliveryState.CART)
    created_on = models.DateTimeField(auto_now_add=True)