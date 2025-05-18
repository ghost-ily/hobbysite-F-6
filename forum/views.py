from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import ThreadCategory, Thread
from .forms import ThreadForm


def list_threads(request):
    threads = Thread.objects.all()
    categories = ThreadCategory.objects.all()
    ctx = {
        'threads':threads,
        'categories':categories
    }
    return render(request, 'post_list.html', ctx)


class CreateThreadView(CreateView):
    form_class = ThreadForm
    success_url = 'forum:post_list'
    template_name = 'post_form.html'


class PostDetailView(DetailView):
    model = Thread
    template_name = 'post_detail.html'

# Create your views here.
