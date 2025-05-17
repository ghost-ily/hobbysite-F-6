from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    ctx = {
        'blog': 'blog/articles',
        'merchstore': 'merchstore/items',
        'forum': 'forum/threads',
        'commissions': 'commissions/list',
        'wiki': 'wiki/articles'
    }
    return render(request, 'homepage.html', ctx)