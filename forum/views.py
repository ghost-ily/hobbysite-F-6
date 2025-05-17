from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import ThreadCategory, Thread


def list_threads(request):
    threads = Thread.objects.all()
    categories = ThreadCategory.objects.all()
    ctx = {
        'threads':threads,
        'categories':categories
    }
    return render(request, 'post_list.html', ctx)
    
    
class PostDetailView(DetailView):
    model = Thread
    template_name = 'post_detail.html'

# Create your views here.
