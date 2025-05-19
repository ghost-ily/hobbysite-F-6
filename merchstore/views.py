from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, ProductType

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

def index(request):
    return HttpResponse('Hello world! Go to /merchstore/items to begin.')