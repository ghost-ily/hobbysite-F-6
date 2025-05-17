from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import NewUserForm

# Create your views here.

@login_required
def display_home(request):
    ctx = {
        'blog': 'blog/articles',
        'merchstore': 'merchstore/items',
        'forum': 'forum/threads',
        'commissions': 'commissions/list',
        'wiki': 'wiki/articles'
    }
    return render(request, 'homepage.html', ctx)


@login_required
def create_user(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            return redirect('login')
    return render(request, 'register_user.html', {'form': form})