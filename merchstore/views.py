from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from .models import Product, ProductType, Transaction
from .forms import ProductForm, TransactionForm
from user_management.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class ProductListView(ListView):
    model = Product
    template_name = 'list.html'

    def get_queryset(self):
        qs = Product.objects.all()
        if self.request.user.is_authenticated:
            user_products = qs.filter(seller=self.request.user.profile)
            others = qs.exclude(seller=self.request.user.profile)
            return list(user_products) + list(others)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_products'] = Product.objects.filter(seller=self.request.user.profile)
            context['other_products'] = Product.objects.exclude(seller=self.request.user.profile)
        else:
            context['other_products'] = Product.objects.all()
        return context

class ProductDetailView(DetailView):   # Checked and fixed by MoochieTenorio, thank you very much!
    model = Product
    form_class = TransactionForm
    template_name = 'detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TransactionForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.buyer = self.request.user.profile
                transaction.product = self.object

                if transaction.amount > self.object.stock:
                    form.add_error('amount', 'Not enough stock available.')
                    return self.render_to_response(self.get_context_data(form=form))

                self.object.stock -= transaction.amount
                self.object.save()
                transaction.save()

                return redirect('merchstore:cart')
            else:
                return self.render_to_response(self.get_context_data(form=form))
        else:
            return redirect('login')

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('merchstore:detail', kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.set_product_status()
        return response

    def get_success_url(self):
        return reverse_lazy('merchstore:detail', kwargs={"pk": self.object.pk})


class CartListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'cartlist.html'

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile)


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactionlist.html'

    def get_queryset(self):
        return Transaction.objects.filter(product__seller=self.request.user.profile)


def index(request):
    return HttpResponse('Welcome to the Hobbysite F-6 Merchstore! Go to /merchstore/items to begin.')
