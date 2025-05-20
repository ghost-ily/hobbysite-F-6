from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, ProductType, Transaction
from django.urls import reverse_lazy
from django.views import View
from .forms import ProductForm, TransactionForm
from user_management.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'list.html'

class ProductDetailView(DetailView):
    model = Product
    form_class = TransactionForm
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TransactionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.buyer = self.request.user.profile
            transaction.product.stock = transaction.product.stock - transaction.amount
            transaction.save()

            return redirect('merchstore:cart')
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

    def get_success_url(self):
        return redirect('merchstore/cart')

class ProductCreateView(LoginRequiredMixin, View):
    def get(self, request):
        product_form = ProductForm()
        return render(request, 'create.html', {
            'form': product_form,
            'view': {'title': 'Add a Product'}
        })
    
    def post(self, request):
        product_form = ProductForm(request.POST)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.owner = self.request.user.profile
            product.save()

            return redirect('merchstore:detail')
        
        return render(request, 'create.html'), {
            'form': product_form,
            'view': {'title': 'Add a Product'}
        }
    
    def get_success_url(self):
        return reverse_lazy('merchstore:detail', kwargs={"pk" : self.kwargs["pk"]})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
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