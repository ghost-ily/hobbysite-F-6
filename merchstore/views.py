from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, ProductType, Transaction
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['product'] = Product.objects.all()
        ctx['form'] = ProductForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset()
            ctx = self.get_context_data(**kwargs)
            ctx['form'] = form
            return self.return_to_response(ctx)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create.html'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'create.html'

    def get_success_url(self):
        return reverse_lazy('merchstore:detail', kwargs={"pk" : self.kwargs["pk"]})

class CartListView(ListView):
    model = Transaction
    template_name = 'cartlist.html'

class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactionlist.html'

def index(request):
    return HttpResponse('Welcome to the Hobbysite F-6 Merchstore! Go to /merchstore/items to begin.')