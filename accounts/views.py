from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from user_management.models import Profile
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


def create_user(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            profile.display_name = username
            profile.email = form.cleaned_data.get('email')
            profile.save()
            return redirect('login')
    return render(request, 'register_user.html', {'form': form})